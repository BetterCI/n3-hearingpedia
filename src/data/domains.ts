export const domains = [
  { id: 'acoustics', name: 'Acoustics', zh: '声学基础', note: '从频率、声级到频谱，建立描述声音的语言。', symbol: '∿' },
  { id: 'ear-cochlea', name: 'Ear & Cochlea', zh: '耳与耳蜗', note: '连接耳蜗结构、力学过程与频率分析。', symbol: '◎' },
  { id: 'neuroscience', name: 'Auditory Neuroscience', zh: '听觉神经科学', note: '理解声音信息如何进入并通过神经系统。', symbol: '⋈' },
  { id: 'psychoacoustics', name: 'Psychoacoustics', zh: '心理声学', note: '用感知实验研究听觉系统的能力与边界。', symbol: '◌' },
  { id: 'binaural', name: 'Spatial & Binaural Hearing', zh: '空间与双耳听觉', note: '探索双耳线索、声源定位与空间感知。', symbol: '↔' },
  { id: 'speech', name: 'Speech Perception', zh: '语音感知', note: '从声学线索走向语音识别与可懂度。', symbol: '≋' },
  { id: 'hearing-loss', name: 'Hearing Loss', zh: '听力损失', note: '理解听觉功能的变化及其研究问题。', symbol: '↘' },
  { id: 'audiology', name: 'Audiology', zh: '听力学', note: '连接听觉测量、测试材料与结果解释。', symbol: '⌁' },
  { id: 'hearing-aids', name: 'Hearing Aids', zh: '助听器', note: '理解放大、压缩与声音处理的设计。', symbol: '⊕' },
  { id: 'cochlear-implants', name: 'Cochlear Implants', zh: '人工耳蜗', note: '连接声音编码、电刺激与感知表现。', symbol: '⋮' },
  { id: 'signal-processing', name: 'Auditory Signal Processing', zh: '听觉信号处理', note: '以滤波、包络和声码器拆解研究方法。', symbol: '⌘' },
  { id: 'ai-hearing', name: 'AI for Hearing', zh: 'AI 与听觉', note: '探索数据、模型与听觉研究的交叉问题。', symbol: '✳' },
] as const;

export const domainById = Object.fromEntries(domains.map(d => [d.id, d]));
export const relationLabels = { prerequisite: '前置知识', mechanism: '机制连接', application: '应用连接', method: '研究方法', related: '相关概念' };
