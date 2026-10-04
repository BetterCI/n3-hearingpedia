export const learningPaths = [
  { id: 'mechanisms', title: '从耳蜗到语音感知', english: 'Mechanisms → Perception', description: '适合建立基础：沿着结构、频率分析与掩蔽，理解语音实验的背景。', slugs: ['cochlea', 'tonotopy', 'auditory-filter', 'masking', 'speech-intelligibility'] },
  { id: 'engineering', title: '从信号到人工耳蜗', english: 'Signal → Electric hearing', description: '适合阅读编码与声码器论文：先理解包络，再连接模拟方法和评价指标。', slugs: ['temporal-envelope', 'vocoder', 'speech-intelligibility', 'cochlear-implant'] },
  { id: 'pitch', title: '从周期性到音高编码', english: 'Periodicity → Pitch coding', description: '先区分物理量与知觉，再比较 TLE 与 F0inTFS 的机制及验证范围。', slugs: ['fundamental-frequency', 'temporal-fine-structure', 'amplitude-modulation', 'pitch-perception', 'n-of-m-coding', 'temporal-limits-encoder', 'f0-in-tfs'] },
  { id: 'sparse-speech', title: '从通道选择到稀疏语音', english: 'Channels → Sparse speech', description: '把电编码、逐脉冲声学模拟与双耳信息利用连起来。', slugs: ['n-of-m-coding', 'channel-interaction', 'get-vocoder', 'binaural-integration', 'atomic-speech-model'] },
  { id: 'mandarin', title: '读懂普通话感知实验', english: 'Mandarin → Perceptual patterns', description: '从基频和谐波关系理解声调任务，再用混淆矩阵读出识别模式。', slugs: ['fundamental-frequency', 'harmonicity', 'pitch-perception', 'mandarin-lexical-tone', 'speech-intelligibility', 'confusion-matrix'] },
  { id: 'screening', title: '从测听到远程筛查', english: 'Audiometry → Remote screening', description: '先理解测量与校准，再比较噪声下阈值及双耳测试版本。', slugs: ['pure-tone-audiometry', 'audiometric-calibration', 'speech-reception-threshold', 'zodiac-in-noise', 'interaural-time-difference', 'binaural-intelligibility-level-difference'] },
];
