export const knowledgeAreas = [
  { id: 'sound', title: '声学与信号表征', english: 'Sound & representation', color: '#71d7f6', note: '描述声音的物理量、谱结构与时域表示。' },
  { id: 'biology', title: '结构与听觉机制', english: 'Structure & mechanisms', color: '#a3abff', note: '连接听觉器官、功能机制、损伤与适应。' },
  { id: 'perception', title: '听觉与语言感知', english: 'Auditory perception', color: '#65e1bb', note: '研究听者如何检测、分组和理解声音。' },
  { id: 'mandarin-consonants', title: '普通话辅音感知', english: 'Mandarin consonant perception', color: '#c6a0f6', note: '从普通话辅音的语音学基础，逐步理解声学线索与感知。' },
  { id: 'measurement', title: '听力与功能测量', english: 'Hearing assessment', color: '#f3c777', note: '定义测试、标度、指标与结果解释。' },
  { id: 'technology', title: '听觉技术与康复', english: 'Hearing technology', color: '#ee9bd2', note: '连接助听器、人工耳蜗、声音编码和康复。' },
  { id: 'methods', title: '研究方法与模型', english: 'Methods & models', color: '#ff9a83', note: '组织声学模拟、稀疏表示和行为数据分析。' },
] as const;
export const knowledgeAreaById = Object.fromEntries(knowledgeAreas.map(a => [a.id, a]));
export const kindLabels = {
  discipline: '研究领域',
  anatomy: '解剖结构', organization: '组织关系', quantity: '物理量／声学属性',
  representation: '信号表征', phenomenon: '感知现象', 'acoustic-environment': '声学现象与环境', function: '感知功能', linguistic: '语言类别',
  mechanism: '功能机制', condition: '听觉损伤／病理状态', 'physiological-response': '神经生理反应', metric: '评价指标', test: '测量方法／测试',
  calibration: '校准方法', technology: '听觉技术', strategy: '编码策略',
  model: '研究模型', analysis: '数据分析方法',
} as const;
