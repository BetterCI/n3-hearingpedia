"""CI coding teaching models. No clinical current units or hardware output.

Python 3 + numpy + scipy. Run: python teaching_encoder.py --out ci-demo
All amplitudes are dimensionless. Not a commercial encoder implementation.
"""
from pathlib import Path
import argparse
import json
import numpy as np
from scipy import signal

FS = 24000
M = 8
RATE = 800  # selection cycles/s, not the audio sampling rate
TAU = 25e-6
GAP = 8e-6
SLOT = 2 * TAU + GAP


def analyse(x, fs=FS, m=M):
    edges = np.geomspace(200, 6000, m + 1)
    bands = np.array([signal.sosfilt(signal.butter(
        3, [lo, hi], btype='bandpass', fs=fs, output='sos'), x)
        for lo, hi in zip(edges[:-1], edges[1:])])
    lowpass = signal.butter(2, 200, fs=fs, output='sos')
    env = np.maximum(signal.sosfilt(lowpass, np.abs(bands), axis=1), 0)
    return bands, env, edges


def compress(env, reference=0.25, floor_db=-50):
    level = 20 * np.log10(np.maximum(env / reference, 1e-12))
    u = np.clip((level - floor_db) / (-floor_db), 0, 1)
    return np.log1p(20 * u) / np.log1p(20)


def select_channels(v, n):
    if not 1 <= n <= len(v):
        raise ValueError('n must be between 1 and number of channels')
    # Equal values: lower teaching channel index wins. Then stimulate by place.
    return np.sort(np.argsort(-v, kind='stable')[:n])


def schedule(env, n, fs=FS, rate=RATE):
    if n * SLOT > 1 / rate:
        raise ValueError('pulses cannot fit into a selection cycle')
    events = []  # [time_s, zero_based_channel, relative_amplitude]
    mapped = compress(env)
    for j in range(int(env.shape[1] / fs * rate)):
        sample = int(j * fs / rate)
        chosen = select_channels(env[:, sample], n)
        for rank, ch in enumerate(chosen):
            events.append([j / rate + rank * SLOT, int(ch), mapped[ch, sample]])
    return np.asarray(events)


def upward_crossings(y, fs=FS):
    idx = np.flatnonzero((y[:-1] < 0) & (y[1:] >= 0))
    frac = -y[idx] / (y[idx + 1] - y[idx])
    return (idx + frac) / fs


def steering(amplitude, alpha):
    if not 0 <= alpha <= 1:
        raise ValueError('alpha outside [0,1]')
    return (1 - alpha) * amplitude, alpha * amplitude


def biphasic(t, onset, amplitude):
    local = t - onset
    return amplitude * (((local >= 0) & (local < TAU)).astype(float)
                        - ((local >= TAU + GAP) & (local < SLOT)).astype(float))


def demo():
    t = np.arange(int(0.12 * FS)) / FS
    x = ((0.55 + 0.35 * np.sin(2 * np.pi * 40 * t)) *
         (0.18 * np.sin(2 * np.pi * 330 * t) +
          0.12 * np.sin(2 * np.pi * 1100 * t) +
          0.09 * np.sin(2 * np.pi * 2800 * t)))
    bands, env, edges = analyse(x)
    cis, ace = schedule(env, M), schedule(env, 4)
    return t, x, bands, env, edges, cis, ace


def verify(cis, ace):
    # Algorithmic invariants, not physiological safety validation.
    assert len(cis) == 768 and len(ace) == 384
    for events in (cis, ace):
        assert np.all(np.diff(events[:, 0]) >= SLOT - 1e-12)
        assert np.all((events[:, 2] >= 0) & (events[:, 2] <= 1))
    assert np.array_equal(select_channels(np.array([.2, .8, .5, .1]), 2), [1, 2])
    assert np.array_equal(select_channels(np.ones(4), 2), [0, 1])
    assert np.array_equal(compress(np.zeros(8)), np.zeros(8))
    assert np.isclose(compress(np.array([.25]))[0], 1)
    for alpha in (0, .25, .5, .75, 1):
        assert np.isclose(sum(steering(.8, alpha)), .8)
    # A pulse sampled at interval midpoints: equal positive/negative area.
    dt = 1e-6
    tt = (np.arange(100) + .5) * dt
    assert abs(np.sum(biphasic(tt, 0, .8)) * dt) < 1e-15
    tt = np.arange(FS) / FS
    times = upward_crossings(np.sin(2 * np.pi * 300 * tt))
    assert np.max(np.abs(np.diff(times) - 1 / 300)) < 1 / FS
    try:
        schedule(np.ones((8, 30)), 8, rate=10000)
    except ValueError:
        pass
    else:
        raise AssertionError('infeasible timing must be rejected')
    return {'cis_events': len(cis), 'ace_events': len(ace),
            'cycles': 96, 'amplitude_unit': 'dimensionless',
            'checks': 'selection, timing, compression, charge balance, steering, crossings'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('ci-demo'))
    args = parser.parse_args()
    t, x, bands, env, edges, cis, ace = demo()
    report = verify(cis, ace)
    args.out.mkdir(parents=True, exist_ok=True)
    np.savez(args.out / 'teaching-data.npz', t=t, x=x, bands=bands,
             envelope=env, edges=edges, cis=cis, ace=ace)
    for name, events in [('cis', cis), ('ace', ace)]:
        np.savetxt(args.out / (name + '-events.csv'), events, delimiter=',',
                   header='time_s,channel_zero_based,relative_amplitude', comments='')
    (args.out / 'checks.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))
