export {};
// The analyser supplies real audio spectra; the audio clock determines history placement.
const $ = <T extends HTMLElement>(id: string) => document.getElementById(id) as T;
const chart = $<HTMLCanvasElement>('spectrogram');
const wave = $<HTMLCanvasElement>('waveform');
const spectrum = $<HTMLCanvasElement>('spectrum');
const history = document.createElement('canvas');
const historyCtx = history.getContext('2d')!;
const chartCtx = chart.getContext('2d')!;
const waveCtx = wave.getContext('2d')!;
const spectrumCtx = spectrum.getContext('2d')!;
const fft = $<HTMLSelectElement>('fft');
const scale = $<HTMLSelectElement>('scale');
const maxFrequency = $<HTMLSelectElement>('max-frequency');
const palette = $<HTMLSelectElement>('palette');
const duration = $<HTMLSelectElement>('duration');
const range = $<HTMLInputElement>('range');
const preset = $<HTMLSelectElement>('preset');
const listen = $<HTMLInputElement>('listen');
const pauseButton = $<HTMLButtonElement>('pause');
const stopButton = $<HTMLButtonElement>('stop');
const overlay = $('start-overlay');
type Mode = 'demo' | 'mic' | 'file';
type State = 'idle' | 'running' | 'paused' | 'loading' | 'error';
let context: AudioContext | undefined;
let analyser: AnalyserNode | undefined;
let monitor: GainNode | undefined;
let source: AudioBufferSourceNode | MediaStreamAudioSourceNode | undefined;
let stream: MediaStream | undefined;
let frequencies = new Float32Array(1024);
let samples = new Float32Array(2048);
let mode: Mode = 'demo';
let state: State = 'idle';
let operation = 0;
let frame = 0;
let lastAudioTime = 0;
let fraction = 0;
let lastStats = 0;
let width = 1000, height = 400;
const left = 52, right = 20, top = 18, bottom = 30;
const minimumFrequency = 50;
const dbCeiling = -15;
let lut: number[][] = [];
let rowBins: [number, number][] = [];
const presets: Record<string, string> = {
  vowel: '元音变换：a → i → u；观察明亮频带的位置变化。',
  harmonics: '谐波阶梯：基频 220 Hz，每两秒增加一组谐波。',
  sweep: '频率扫掠：180–6000 Hz，观察频率轨迹的往返变化。',
  pulse: '短脉冲：每 0.75 秒出现一次宽频瞬态，比较不同 FFT 点数。',
};

function message(text: string, error = false) {
  $('message').textContent = text;
  $('message').classList.toggle('error', error);
}

function setState(value: State) {
  state = value;
  $('live-status').dataset.state = value;
  $('state-label').textContent = {idle: 'READY / 准备就绪', running: 'LIVE / 实时分析', paused: 'PAUSED / 已暂停', loading: 'LOADING / 正在连接', error: 'NOTICE / 请检查输入'}[value];
  pauseButton.disabled = !['running', 'paused'].includes(value);
  stopButton.disabled = ['idle', 'error'].includes(value);
  pauseButton.textContent = value === 'paused' ? '▷ 继续' : 'Ⅱ 暂停';
  // Keep the demo action available if a microphone permission prompt is pending.
  listen.disabled = mode === 'mic';
}

function maximum() { return Math.min(Number(maxFrequency.value), (context?.sampleRate ?? 48000) / 2); }
function frequencyAt(position: number) {
  return scale.value === 'log'
    ? minimumFrequency * (maximum() / minimumFrequency) ** position
    : minimumFrequency + (maximum() - minimumFrequency) * position;
}
function yAt(frequency: number) {
  const position = scale.value === 'log'
    ? Math.log(frequency / minimumFrequency) / Math.log(maximum() / minimumFrequency)
    : (frequency - minimumFrequency) / (maximum() - minimumFrequency);
  return top + (1 - position) * (height - top - bottom);
}

function updatePalette() {
  const colors: Record<string, number[][]> = {
    aurora: [[9,11,20], [40,26,80], [104,43,144], [202,67,178], [245,155,198], [157,255,226]],
    ember: [[9,11,20], [66,19,61], [152,34,75], [230,82,51], [255,177,75], [255,248,199]],
    ice: [[9,11,20], [18,39,90], [28,89,159], [47,164,203], [120,229,234], [222,255,251]],
  };
  const stops = colors[palette.value];
  lut = Array.from({length: 256}, (_, i) => {
    const p = i / 255 * (stops.length - 1), index = Math.min(stops.length - 2, Math.floor(p)), t = p - index;
    return stops[index].map((v, c) => Math.round(v + (stops[index + 1][c] - v) * t));
  });
  $('color-key').style.background = `linear-gradient(90deg,${stops.map(c => `rgb(${c.join(',')})`).join(',')})`;
}

function updateBins() {
  const binHz = (context?.sampleRate ?? 48000) / Number(fft.value);
  rowBins = Array.from({length: history.height}, (_, y) => {
    const a = frequencyAt(1 - (y + 1) / history.height) / binHz;
    const b = frequencyAt(1 - y / history.height) / binHz;
    return [Math.max(1, Math.floor(a)), Math.min(frequencies.length - 1, Math.max(Math.floor(a), Math.ceil(b)))];
  });
}

function updateInfo() {
  $('axis-caption').textContent = `${scale.value === 'log' ? '对数' : '线性'}刻度 · Hz`;
  $('time-caption').textContent = `最近 ${duration.value} s`;
  $('range-output').textContent = `${range.value} dB`;
  $('db-floor').textContent = `−${Number(range.value) - dbCeiling} dB`;
  if (context) {
    const n = Number(fft.value), rate = context.sampleRate;
    $('analysis-info').textContent = `${(rate / 1000).toFixed(1)} kHz · Blackman 窗 ${(n / rate * 1000).toFixed(1)} ms · 栅格 ${(rate / n).toFixed(1)} Hz · 平滑 0`;
  }
}

function clearHistory() {
  historyCtx.fillStyle = '#090b14';
  historyCtx.fillRect(0, 0, history.width, history.height);
  fraction = 0;
  lastAudioTime = context?.currentTime ?? 0;
  updateBins(); updateInfo(); paintChart();
}

function sizeCanvas(canvas: HTMLCanvasElement) {
  const rect = canvas.getBoundingClientRect(), dpr = Math.min(devicePixelRatio || 1, 2);
  canvas.width = Math.round(rect.width * dpr); canvas.height = Math.round(rect.height * dpr);
  canvas.getContext('2d')!.setTransform(dpr, 0, 0, dpr, 0, 0);
  return rect;
}

function resize() {
  const old = document.createElement('canvas'); old.width = history.width; old.height = history.height;
  old.getContext('2d')!.drawImage(history, 0, 0);
  const rect = sizeCanvas(chart); width = rect.width; height = rect.height;
  history.width = Math.max(1, Math.round(width - left - right)); history.height = Math.max(1, Math.round(height - top - bottom));
  historyCtx.fillStyle = '#090b14'; historyCtx.fillRect(0, 0, history.width, history.height);
  historyCtx.drawImage(old, 0, 0, history.width, history.height);
  sizeCanvas(wave); sizeCanvas(spectrum); updateBins(); paintChart(); paintScopes();
}

function paintChart() {
  chartCtx.fillStyle = '#090b14'; chartCtx.fillRect(0, 0, width, height);
  chartCtx.drawImage(history, left, top, width - left - right, height - top - bottom);
  chartCtx.font = '9px ui-monospace, Consolas, monospace';
  const ticks = scale.value === 'log' ? [50,100,200,500,1000,2000,4000,8000,16000] : [50,1000,2000,4000,6000,8000,12000,16000];
  if (!ticks.includes(maximum())) ticks.push(maximum());
  chartCtx.textAlign = 'right';
  for (const frequency of ticks.filter(f => f >= minimumFrequency && f <= maximum())) {
    const y = yAt(frequency);
    chartCtx.strokeStyle = '#c5b2ef12'; chartCtx.beginPath(); chartCtx.moveTo(left, y); chartCtx.lineTo(width - right, y); chartCtx.stroke();
    chartCtx.fillStyle = '#a394b7'; chartCtx.fillText(frequency >= 1000 ? `${frequency / 1000}k` : `${frequency}`, left - 10, y + 3);
  }
  for (let i = 0; i <= 4; i++) {
    const x = left + (width - left - right) * i / 4;
    chartCtx.strokeStyle = '#c5b2ef12'; chartCtx.beginPath(); chartCtx.moveTo(x, top); chartCtx.lineTo(x, height - bottom); chartCtx.stroke();
    chartCtx.fillStyle = '#a394b7'; chartCtx.textAlign = i === 4 ? 'right' : i === 0 ? 'left' : 'center';
    chartCtx.fillText(i === 4 ? '现在' : `−${Number(duration.value) * (1 - i / 4)} s`, x, height - 10);
  }
  chartCtx.strokeStyle = '#a9ffe0aa'; chartCtx.beginPath(); chartCtx.moveTo(width - right, top); chartCtx.lineTo(width - right, height - bottom); chartCtx.stroke();
}

function paintScopes() {
  const w = wave.clientWidth, h = wave.clientHeight, sw = spectrum.clientWidth, sh = spectrum.clientHeight;
  waveCtx.clearRect(0, 0, w, h); spectrumCtx.clearRect(0, 0, sw, sh);
  waveCtx.strokeStyle = '#92f5d4'; waveCtx.lineWidth = 1; waveCtx.beginPath();
  // Show a fixed 20 ms slice, rather than changing waveform scale with FFT size.
  const count = Math.min(samples.length, Math.floor((context?.sampleRate ?? 48000) * .02));
  for (let x = 0; x < w; x++) {
    const value = samples[Math.min(samples.length - 1, Math.floor(x / w * count))] || 0;
    const y = h / 2 - value * h * .44;
    if (!x) waveCtx.moveTo(x, y); else waveCtx.lineTo(x, y);
  }
  waveCtx.stroke();
  spectrumCtx.beginPath(); spectrumCtx.moveTo(0, sh);
  const floor = dbCeiling - Number(range.value), hz = (context?.sampleRate ?? 48000) / Number(fft.value);
  for (let x = 0; x < sw; x++) {
    const index = Math.min(frequencies.length - 1, Math.max(1, Math.round(frequencyAt(x / sw) / hz)));
    const value = Math.max(0, Math.min(1, ((frequencies[index] ?? floor) - floor) / Number(range.value)));
    spectrumCtx.lineTo(x, sh - value * sh * .94);
  }
  spectrumCtx.lineTo(sw, sh); spectrumCtx.closePath();
  const gradient = spectrumCtx.createLinearGradient(0, 0, 0, sh); gradient.addColorStop(0, '#c49cff80'); gradient.addColorStop(1, '#9d6af508');
  spectrumCtx.fillStyle = gradient; spectrumCtx.fill(); spectrumCtx.strokeStyle = '#c5a3f5'; spectrumCtx.lineWidth = 1; spectrumCtx.stroke();
}

function animate() {
  if (state !== 'running' || !context || !analyser) return;
  analyser.getFloatFrequencyData(frequencies); analyser.getFloatTimeDomainData(samples);
  const now = context.currentTime, elapsed = Math.max(0, now - lastAudioTime);
  fraction += elapsed * history.width / Number(duration.value); lastAudioTime = now;
  const advance = Math.floor(fraction); fraction -= advance;
  if (advance > 0) {
    const shift = Math.min(advance, history.width);
    historyCtx.drawImage(history, -shift, 0);
    historyCtx.fillStyle = '#090b14'; historyCtx.fillRect(history.width - shift, 0, shift, history.height);
    // A background-tab gap has no acquired frames. Keep it blank instead of inventing history.
    const stripeWidth = elapsed > .2 ? 1 : shift;
    const stripe = historyCtx.createImageData(1, history.height), floor = dbCeiling - Number(range.value);
    for (let y = 0; y < history.height; y++) {
      const [start, end] = rowBins[y]; let db = -Infinity;
      for (let k = start; k <= end; k++) db = Math.max(db, frequencies[k]);
      const index = Math.max(0, Math.min(255, Math.round((db - floor) / Number(range.value) * 255)));
      const color = lut[index];
      stripe.data.set([color[0], color[1], color[2], 255], y * 4);
    }
    historyCtx.putImageData(stripe, history.width - 1, 0);
    if (stripeWidth > 1) historyCtx.drawImage(history, history.width - 1, 0, 1, history.height, history.width - stripeWidth, 0, stripeWidth, history.height);
  }
  paintChart(); paintScopes();
  if (now - lastStats > .12) {
    let peak = -Infinity, index = 0, amplitude = 0;
    for (let k = 1; k < frequencies.length; k++) {
      const f = k * context.sampleRate / analyser.fftSize;
      if (f >= minimumFrequency && f <= maximum() && frequencies[k] > peak) { peak = frequencies[k]; index = k; }
    }
    for (const sample of samples) amplitude = Math.max(amplitude, Math.abs(sample));
    $('peak-stat').textContent = peak > -100 ? `${Math.round(index * context.sampleRate / analyser.fftSize)} Hz` : '— Hz';
    $('level-stat').textContent = amplitude > 1e-7 ? `${(20 * Math.log10(amplitude)).toFixed(1)} dBFS` : '−∞ dBFS';
    lastStats = now;
  }
  frame = requestAnimationFrame(animate);
}

function disconnect() {
  cancelAnimationFrame(frame);
  if (source instanceof AudioBufferSourceNode) { source.onended = null; try { source.stop(); } catch { /* Already ended. */ } }
  source?.disconnect(); source = undefined;
  stream?.getTracks().forEach(track => track.stop()); stream = undefined;
  analyser?.disconnect(); monitor?.disconnect();
}

function stop() {
  operation++; disconnect(); void context?.suspend(); setState('idle');
  samples.fill(0); frequencies.fill(-Infinity); paintScopes();
  $('peak-stat').textContent = '— Hz'; $('level-stat').textContent = '— dBFS';
  message('已停止，音频输入已释放。图像保留，可保存或重新开始。');
}

// Deterministic teaching signals: generated PCM is analysed through the same path as other sources.
function synthesize(audio: AudioContext, name: string) {
  const seconds = name === 'harmonics' ? 8 : name === 'pulse' ? 6 : 9;
  const buffer = audio.createBuffer(1, audio.sampleRate * seconds, audio.sampleRate), data = buffer.getChannelData(0);
  let phase = 0, maximumAmplitude = 0, noiseSeed = 4127;
  const formants = [[730,1090,2440], [270,2290,3010], [300,870,2240]];
  for (let n = 0; n < data.length; n++) {
    const t = n / audio.sampleRate; let value = 0;
    if (name === 'sweep') {
      const f = 180 * (6000 / 180) ** ((1 - Math.cos(2 * Math.PI * t / seconds)) / 2);
      phase += 2 * Math.PI * f / audio.sampleRate; value = Math.sin(phase) * .6;
    } else if (name === 'pulse') {
      noiseSeed = (Math.imul(noiseSeed, 1664525) + 1013904223) >>> 0;
      const distance = t % .75 - .1;
      value = (noiseSeed / 4294967296 * 2 - 1) * Math.exp(-.5 * (distance / .003) ** 2);
    } else {
      const f0 = name === 'harmonics' ? 220 : 140;
      phase += 2 * Math.PI * f0 / audio.sampleRate;
      const p = t / 3, a = Math.floor(p) % 3, b = (a + 1) % 3;
      const blend = Math.max(0, Math.min(1, (p % 1 - .5) * 2));
      const bands = formants[a].map((v, i) => v * (1 - blend) + formants[b][i] * blend);
      const harmonics = name === 'harmonics' ? 3 + Math.floor(t / 2) * 4 : 38;
      for (let k = 1; k <= harmonics; k++) {
        const f = k * f0;
        const weight = name === 'harmonics' ? 1 / k : (.025 + bands.reduce((sum, center) => sum + Math.exp(-.5 * ((f - center) / 100) ** 2), 0)) / Math.sqrt(k);
        value += Math.sin(k * phase) * weight;
      }
    }
    // Fade boundaries to keep the loop junction from introducing a broadband click.
    value *= Math.min(1, t / .025, (seconds - t) / .025);
    data[n] = value; maximumAmplitude = Math.max(maximumAmplitude, Math.abs(value));
  }
  const gain = .65 / Math.max(.001, maximumAmplitude);
  for (let n = 0; n < data.length; n++) data[n] *= gain;
  return buffer;
}

function errorMessage(error: unknown) {
  const name = error instanceof Error ? error.name : '';
  if (name === 'NotAllowedError' || name === 'SecurityError') return '麦克风访问未获允许。请在浏览器网站权限中开启，或使用「合成演示」与本地音频。';
  if (name === 'NotFoundError') return '未找到麦克风。可以接入设备后重试，或先体验合成演示。';
  if (name === 'NotReadableError') return '麦克风暂时无法读取，可能正被其他应用占用。请检查设备后重试。';
  return error instanceof Error ? error.message : '无法读取音频，请换一个文件或使用合成演示。';
}

async function start(nextMode: Mode, file?: File) {
  const ticket = ++operation; disconnect(); mode = nextMode; setState('loading');
  message(nextMode === 'mic' ? '等待麦克风授权；也可以随时改用合成演示。' : '正在准备声音…');
  try {
    if (!window.AudioContext) throw new Error('当前浏览器不支持 Web Audio，请使用新版浏览器。');
    context ??= new AudioContext(); await context.resume();
    if (ticket !== operation) return;
    analyser = context.createAnalyser(); analyser.fftSize = Number(fft.value); analyser.smoothingTimeConstant = 0;
    monitor = context.createGain(); monitor.gain.value = nextMode !== 'mic' && listen.checked ? .35 : 0;
    analyser.connect(monitor); monitor.connect(context.destination);
    if (nextMode === 'mic') {
      if (!navigator.mediaDevices?.getUserMedia) throw new Error('麦克风需要 HTTPS 或 localhost 环境。当前可使用合成演示或本地音频。');
      const acquired = await navigator.mediaDevices.getUserMedia({audio: {echoCancellation: false, noiseSuppression: false, autoGainControl: false}, video: false});
      if (ticket !== operation) { acquired.getTracks().forEach(track => track.stop()); return; }
      stream = acquired; source = context.createMediaStreamSource(stream);
      const track = stream.getAudioTracks()[0]; track.addEventListener('ended', () => { if (ticket === operation) { stop(); message('麦克风连接已结束，请重新开启或切换输入。'); } });
      const settings = track.getSettings();
      const setting = (value: boolean | undefined) => value === undefined ? '未报告' : value ? '开' : '关';
      message(`麦克风已连接，不回放声音。设备报告：降噪${setting(settings.noiseSuppression)} / 自动增益${setting(settings.autoGainControl)} / 回声消除${setting(settings.echoCancellation)}。`);
    } else {
      let buffer: AudioBuffer;
      if (nextMode === 'file') {
        if (!file) throw new Error('请先选择本地音频。');
        if (file.size > 80 * 1024 * 1024) throw new Error('请选择小于 80 MB 的音频文件，以控制浏览器内存占用。');
        const encoded = await file.arrayBuffer();
        if (ticket !== operation) return;
        try { buffer = await context.decodeAudioData(encoded); } catch { throw new Error('无法解码此音频。请尝试 WAV、MP3 或浏览器支持的音频格式。'); }
        if (ticket !== operation) return;
      } else buffer = synthesize(context, preset.value);
      const player = context.createBufferSource(); player.buffer = buffer; player.loop = nextMode === 'demo'; source = player;
      player.onended = () => { if (ticket === operation) { stop(); message('音频播放完毕。图像已保留，可以保存或再次选择文件。'); } };
      message(nextMode === 'demo' ? `${presets[preset.value]} ${listen.checked ? '正在播放声音。' : '当前静音，可勾选「播放声音」。'}` : `本地文件：${file!.name} · ${buffer.duration.toFixed(1)} s · ${listen.checked ? '声音已开启' : '静音分析，可勾选播放声音'}`);
    }
    source.connect(analyser);
    frequencies = new Float32Array(analyser.frequencyBinCount); frequencies.fill(-Infinity);
    samples = new Float32Array(analyser.fftSize); clearHistory(); lastStats = 0;
    overlay.hidden = true; setState('running');
    if (source instanceof AudioBufferSourceNode) source.start();
    animate();
  } catch (error) {
    if (ticket !== operation) return;
    disconnect(); void context?.suspend(); setState('error'); message(errorMessage(error), true);
  }
}

$('quick-start').addEventListener('click', () => void start('demo'));
$('demo').addEventListener('click', () => void start('demo'));
$('microphone').addEventListener('click', () => void start('mic'));
$('stop').addEventListener('click', stop);
$<HTMLInputElement>('audio-file').addEventListener('change', event => {
  const input = event.target as HTMLInputElement, file = input.files?.[0];
  if (file) void start('file', file); input.value = '';
});
preset.addEventListener('change', () => { if (mode === 'demo' && ['running', 'paused'].includes(state)) void start('demo'); });
listen.addEventListener('change', () => { if (context && monitor) monitor.gain.setTargetAtTime(mode !== 'mic' && listen.checked ? .35 : 0, context.currentTime, .02); });
pauseButton.addEventListener('click', async () => {
  if (!context || !['running', 'paused'].includes(state)) return;
  const ticket = operation;
  pauseButton.disabled = true;
  try {
    if (state === 'running') {
      cancelAnimationFrame(frame); await context.suspend();
      if (ticket === operation) { setState('paused'); message('已暂停声音与分析。可以保存当前图像，点击「继续」恢复。'); }
    } else {
      await context.resume();
      if (ticket === operation) { lastAudioTime = context.currentTime; setState('running'); message('已继续实时分析。'); animate(); }
    }
  } catch { if (ticket === operation) { stop(); message('浏览器未能恢复音频，请重新选择输入。', true); } }
});

for (const element of [fft, scale, maxFrequency, duration, palette, range]) {
  element.addEventListener(element === range ? 'input' : 'change', () => {
    if (analyser && element === fft) { analyser.fftSize = Number(fft.value); frequencies = new Float32Array(analyser.frequencyBinCount); frequencies.fill(-Infinity); samples = new Float32Array(analyser.fftSize); }
    if (element === palette) updatePalette();
    clearHistory(); paintScopes();
  });
}

$('snapshot').addEventListener('click', () => {
  const image = document.createElement('canvas'); image.width = chart.width; image.height = chart.height + 88;
  const ctx = image.getContext('2d')!;
  ctx.fillStyle = '#0c0c16'; ctx.fillRect(0, 0, image.width, image.height); ctx.drawImage(chart, 0, 0);
  ctx.fillStyle = '#c9b8e1'; ctx.font = '12px sans-serif';
  ctx.fillText(`n³ Hearingpedia / Spectrogram · ${new Date().toLocaleString('zh-CN')}`, 24, chart.height + 24);
  ctx.font = '10px sans-serif';
  const sourceLabel = mode === 'demo' ? `合成 ${preset.selectedOptions[0].text}` : mode === 'mic' ? '麦克风' : '本地音频';
  ctx.fillText(`${sourceLabel} · FFT ${fft.value} · ${scale.value} · ${minimumFrequency}–${maximum()} Hz · ${duration.value} s · Blackman · ${(context?.sampleRate ?? 0)} Hz`, 24, chart.height + 45);
  ctx.fillText(`颜色：Web Audio 谱幅 ${dbCeiling - Number(range.value)} 至 ${dbCeiling} dB · ${palette.value} · 未校准声压级`, 24, chart.height + 65);
  image.toBlob(blob => { if (!blob) return; const href = URL.createObjectURL(blob), anchor = document.createElement('a'); anchor.href = href; anchor.download = `hearingpedia-spectrogram-${Date.now()}.png`; anchor.click(); setTimeout(() => URL.revokeObjectURL(href), 10000); });
});
$('fullscreen').addEventListener('click', async () => {
  try { if (document.fullscreenElement) await document.exitFullscreen(); else await $('lab-shell').requestFullscreen(); }
  catch { message('此浏览器暂不支持全屏。可在独立页面中放大窗口。'); }
});
document.addEventListener('fullscreenchange', () => { $('fullscreen').textContent = document.fullscreenElement ? '⛶ 退出全屏' : '⛶ 全屏'; });
window.addEventListener('pagehide', () => { operation++; disconnect(); void context?.close(); context = undefined; setState('idle'); });
window.addEventListener('pageshow', event => { if (event.persisted) { overlay.hidden = false; clearHistory(); message('音频已释放，选择输入即可重新开始。'); } });
const observer = new ResizeObserver(resize); observer.observe($('visualizer'));
frequencies.fill(-Infinity); updatePalette(); resize(); clearHistory();
