"""Publication audit: independent acoustic identities and actual exported WAVs."""
from pathlib import Path
import json
import sys
import wave
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT/'public/code/linear-algebra'))
from experiments import run_experiments, delay_matrix, ridge

report, _ = run_experiments()
rng = np.random.default_rng(20261101)
x = rng.normal(0, .25, 2048)
h = np.zeros(65)
h[[0,24,56]] = [.8,.3,-.15]
np.testing.assert_allclose(delay_matrix(x,65)@h, np.convolve(x,h)[64:len(x)], atol=1e-12)
G = np.array([[1.,.995],[.995,1.]])
observed = G@np.array([1.,.2]) + np.array([.001,-.001])
estimate = ridge(G,observed,1e-5)
np.testing.assert_allclose(G.T@(G@estimate-observed)+1e-5*estimate,0,atol=1e-12)
G0 = np.array([[1.,.5],[1.,.5]])
minimum_norm = np.linalg.pinv(G0)@np.ones(2)
np.testing.assert_allclose(minimum_norm,[.8,.4],atol=1e-12)
np.testing.assert_allclose(minimum_norm@np.array([-.5,1.]),0,atol=1e-12)

audio = {}
for path in sorted((ROOT/'public/audio/linear-algebra').glob('*.wav')):
    with wave.open(str(path),'rb') as stream:
        assert (stream.getframerate(), stream.getnframes(), stream.getnchannels(), stream.getsampwidth()) == (16000,11200,1,2)
        samples = np.frombuffer(stream.readframes(stream.getnframes()),dtype='<i2').astype(np.int32)
    assert np.max(np.abs(samples)) < 32767
    audio[path.stem] = samples
assert len(audio)==4
assert np.max(np.abs(audio['tone-mixture']-audio['tone-1000']-audio['tone-2000']))<=2
frequencies=np.fft.rfftfreq(10880,1/16000)
for name, expected in [('tone-1000',1000),('tone-2000',2000)]:
    spectrum=np.abs(np.fft.rfft(audio[name][160:-160]))
    assert abs(frequencies[np.argmax(spectrum)]-expected)<1e-8

result = {
    'data_type':'original teaching signals; no human or clinical measurements',
    'checks':['complete fixed-seed experiment suite', 'delay matrix versus independent linear convolution',
              'ridge objective stationarity', 'pseudoinverse minimum norm and nullspace orthogonality',
              'actual four WAV headers, durations, unclipped samples, common-gain summation and carrier frequencies'],
    'numpy_version':np.__version__, 'echo':report['echo'],
    'conclusion':'No blocking numerical inconsistency found within the stated teaching models.',
}
target=ROOT/'docs/research/linear-algebra-2026-11-01/publication-validation.json'
target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(result['conclusion'])
