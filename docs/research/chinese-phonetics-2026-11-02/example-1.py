fs = 16000
release = 800
for periodic_onset in [992, 1840]:
    vot_ms = (periodic_onset - release) / fs * 1000
    print('release ms:', release/fs*1000, 'onset ms:', periodic_onset/fs*1000, 'VOT ms:', vot_ms)
