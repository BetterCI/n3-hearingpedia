"""Check delivered PCM files; this is not a listening or SPL calibration test."""
import json
from pathlib import Path
import sys
import wave
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).resolve().parents[3]
results = []
for file in sorted((root / 'public/audio/pure-and-complex-tones').glob('*.wav')):
    with wave.open(str(file), 'rb') as audio:
        channels, width, rate, frames, compression, _ = audio.getparams()
        x = np.frombuffer(audio.readframes(frames), dtype='<i2').astype(float) / 32767
    assert (channels, width, rate, frames, compression) == (1, 2, 48000, 57600, 'NONE')
    assert len(x) == frames and np.isfinite(x).all()
    assert x[0] == 0 and x[-1] == 0
    assert np.max(np.abs(x)) < 0.401
    assert 0.0988 < np.sqrt(np.mean(x*x)) < 0.0994
    results.append({'file': file.name, 'channels': channels, 'sample_width_bytes': width,
                    'sample_rate_hz': rate, 'frames': frames, 'duration_seconds': frames/rate,
                    'whole_file_rms': float(np.sqrt(np.mean(x*x))),
                    'peak_absolute': float(np.max(np.abs(x))), 'endpoints_zero': True,
                    'clipped_samples': int(np.count_nonzero(np.abs(x) >= 1))})
record = {'date': '2026-10-10', 'result': 'passed', 'scope': 'PCM headers, duration, amplitude, fades and clipping; no listening test or acoustic calibration', 'files': results}
Path(__file__).with_name('audio-checks.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(record, ensure_ascii=False, indent=2))
