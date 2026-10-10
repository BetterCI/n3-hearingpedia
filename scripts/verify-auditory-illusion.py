"""Verify exported PCM files independently of floating-point synthesis arrays."""
from pathlib import Path
import json
import wave
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/research/auditory-illusion-2026-10-10'
report = json.loads((DOC / 'figure-audio-verification.json').read_text(encoding='utf-8'))
samples = {}
verified = []
for record in report['audio']:
    with wave.open(str(ROOT / 'public/audio/auditory-illusion' / record['file']), 'rb') as stream:
        assert stream.getframerate() == 44100
        assert stream.getsampwidth() == 2
        assert stream.getnchannels() == record['channels']
        assert stream.getcomptype() == 'NONE'
        assert abs(stream.getnframes() / stream.getframerate() - record['duration_s']) < 1e-9
        data = np.frombuffer(stream.readframes(stream.getnframes()), dtype='<i2').reshape(-1, stream.getnchannels())
        assert np.max(np.abs(data.astype(np.int32))) < 32767
        samples[record['file']] = data
        verified.append({'file': record['file'], 'channels': stream.getnchannels(), 'duration_s': record['duration_s'], 'peak_int16': int(np.max(np.abs(data.astype(np.int32))))})
assert len(samples) == 7
assert np.array_equal(samples['scale-stereo.wav'][:, 0], samples['scale-left.wav'][:, 0])
assert np.array_equal(samples['scale-stereo.wav'][:, 1], samples['scale-right.wav'][:, 0])
for start, end in report['continuity']['gaps_s']:
    assert np.all(samples['continuity-silence.wav'][int(start*44100):int(end*44100)] == 0)
output = {'files': verified, 'pcm_format': '44100 Hz, signed 16-bit little-endian', 'no_clipping': True, 'channel_decomposition_exact': True, 'deleted_intervals_silent': True, 'checks_passed': True}
(DOC / 'wav-verification.json').write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'audio_files': len(samples), 'checks_passed': True}))
