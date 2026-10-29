export const introductoryPaths = [
  {
    id: 'intro-sound-hearing', title: '声音如何变成听觉', english: 'From sound to hearing',
    description: '沿着声音、耳蜗、神经通路和语音识别，建立一幅听觉过程的全景。',
    goal: '能说明物理声音、神经响应与听觉感知之间的联系和区别。',
    prerequisite: '无需先修；先读各词条导言，再读本步指定章节。',
    steps: [
      { slug: 'sound-waves-and-propagation', goal: '说明声音传播时，压力和介质运动如何变化。', sections: ['声音怎样在介质中传递', '频率、周期、波长与声速'] },
      { slug: 'cochlea', goal: '理解耳蜗怎样分析声音并产生神经输入。', sections: ['耳蜗力学与频率分析', '毛细胞的机械电转导'] },
      { slug: 'auditory-pathway', goal: '认识听觉通路中的分支、双侧联系与下行调节。', sections: ['整体组织：主干、分支与双侧联系', '下行调节：改变响应，也参与学习'] },
      { slug: 'speech-perception', goal: '区分声音中的声学线索与听者识别的语音类别。', sections: ['研究对象与解释层次', '声学线索怎样支持识别'] },
    ],
    optional: ['tonotopy', 'phase-locking', 'auditory-scene-analysis'], furtherPath: 'mechanisms',
  },
  {
    id: 'intro-cochlear-implant', title: '理解人工耳蜗', english: 'Understanding cochlear implants',
    description: '从听力损失进入人工耳蜗系统，理解声音编码与电极之间的相互作用。',
    goal: '能解释人工耳蜗的基本流程，以及声音编码为何不能保证恢复全部听觉能力。',
    prerequisite: '建议先了解耳蜗；重点读系统流程与概念，策略目录和模型按需深入。',
    steps: [
      { slug: 'hearing-loss', goal: '区分损伤类型、听阈与阈上听觉能力。', sections: ['类型、病因与病程', '阈上听觉为何重要'] },
      { slug: 'cochlear-implant', goal: '说清外部处理器、植入部件与个体映射的作用。', sections: ['定义与系统组成', '声音编码与个体映射'] },
      { slug: 'cochlear-implant-coding-strategies', goal: '理解编码策略解决什么问题，以及怎样评价策略。', sections: ['定义与知识体系', '策略评价与分析示例'] },
      { slug: 'channel-interaction', goal: '理解名义通道数量与有效独立信息之间的区别。', sections: ['定义与分类', '从电场到有效信息的不同层次'] },
    ],
    optional: ['cochlea', 'cochlear-implant-sound-perception', 'vocoder'], furtherPath: 'technology',
  },
  {
    id: 'intro-hearing-assessment', title: '读懂听力测量', english: 'Reading hearing measurements',
    description: '从评估任务出发，区分纯音、言语测试与校准分别回答的问题。',
    goal: '能读出测量对象、条件与解释边界，理解不同测试为什么需要交叉验证。',
    prerequisite: '无需临床先修；先关注测试任务和单位，具体操作与标准细节按需深入。',
    steps: [
      { slug: 'audiology', goal: '区分筛查、诊断、功能评估和干预评价。', sections: ['学科范围与评估层次', '交叉验证：处理一致与不一致'] },
      { slug: 'pure-tone-audiometry', goal: '理解听阈、听力级与听力图的解释边界。', sections: ['测量对象与基本概念', '听力图判读与解释边界'] },
      { slug: 'speech-audiometry', goal: '区分言语阈值、正确率和噪声中的测试任务。', sections: ['先分清任务与输出指标', '为什么听力图不能替代言语测试'] },
      { slug: 'audiometric-calibration', goal: '理解校准如何把数字幅度连接到实际声学输出。', sections: ['为什么听力测量需要校准', '声压级、听力级与数字幅度'] },
    ],
    optional: ['hearing-loss', 'speech-reception-threshold', 'auditory-brainstem-response'], furtherPath: 'measurement',
  },
];

export const learningPaths = [
  { id:'acoustic-equations',title:'从声传播到时域与频域声学建模',english:'Wave equations and acoustic modelling',description:'从压力与质点运动进入守恒推导、初始条件和边界，再连接单频声场、模态、房间与器件。',slugs:['sound-waves-and-propagation','wave-equation','helmholtz-equation','room-acoustics','electroacoustic-transducer'] },
  { id:'microphone',title:'从声学接收到可解释的听觉实验输入',english:'Microphones and auditory measurements',description:'从换能原理进入声路、指向性与噪声，再用频谱、动态范围和校准连接录音、声学测量及言语评价。',slugs:['electroacoustic-transducer','microphone','spectrum-and-power-spectral-density','dynamic-range','audiometric-calibration','speech-intelligibility'] },
  { id:'electroacoustic-transducer',title:'从物理端口理解电声器件与听觉应用',english:'Electroacoustic transducers',description:'从声波和边界进入换能机制、阻抗及负载，再通过动态范围与校准理解实验刺激、助听器和实际言语评价。',slugs:['sound-waves-and-propagation','electroacoustic-transducer','dynamic-range','audiometric-calibration','pure-tone-audiometry','hearing-aid','speech-intelligibility'] },
  { id:'comparative-hearing',title:'从动物听觉理解人类机制与应用',english:'Comparative hearing & human applications',description:'从传播与双耳时间线索进入跨物种比较，再阅读空间学习、感受细胞修复与仿生助听器的证据边界。',slugs:['sound-waves-and-propagation','interaural-time-difference','comparative-hearing','auditory-plasticity','inner-hair-cell','outer-hair-cell','hearing-aid'] },
  { id:'mandarin-consonants',title:'普通话辅音的语音学基础',english:'Mandarin consonant phonetics',description:'从语音学总览、辅音系统和国际音标进入发音部位与方式，再分别理解送气和清浊。',slugs:['phonetics','speech-perception','mandarin-consonants','consonant-place-of-articulation','consonant-manner-of-articulation','aspiration','voicing'] },
  { id:'sound', title:'声音的物理量与时域表征', english:'Sound & representation', description:'从声波传播进入基频、谐波、共振峰、动态范围与时域表征，理解相同声音的不同表示。', slugs:['sound-waves-and-propagation','pure-and-complex-tones','spectrum-and-power-spectral-density','phase-and-group-delay','cepstrum','fundamental-frequency','harmonicity','formant','spectrogram','amplitude-modulation','temporal-envelope','temporal-fine-structure','dynamic-range','room-acoustics'] },
  { id:'mechanisms',title:'听觉结构、频率分析与感知',english:'Mechanisms & perception',description:'从耳蜗和主动机制进入频率分辨、音高、音色、音乐与言语知觉，再理解注意、努力与经验相关变化。',slugs:['outer-middle-ear-transmission','cochlea','outer-hair-cell','inner-hair-cell','phase-locking','auditory-pathway','auditory-cortex','tonotopy','auditory-filter','auditory-computational-models','frequency-resolution','temporal-resolution','masking','loudness','auditory-scene-analysis','auditory-illusion','pitch-perception','timbre-perception','music-perception','speech-perception','speech-intelligibility','speech-redundancy','mandarin-lexical-tone','auditory-attention','listening-effort','auditory-plasticity','auditory-development','auditory-aging'] },
  { id:'binaural',title:'空间线索与双耳信息利用',english:'Spatial & binaural hearing',description:'从空间任务进入时间关系，区分整合现象和特定双耳阈值指标。',slugs:['binaural-hearing','spatial-hearing','interaural-time-difference','interaural-level-difference','binaural-integration','binaural-intelligibility-level-difference'] },
  { id:'measurement',title:'听力损失与功能评估',english:'Measurement & assessment',description:'从听力学的评估框架进入损伤状态、检测敏感度与神经响应，再比较校准、言语测听任务、阈值和测试条件。',slugs:['audiology','hearing-loss','auditory-development','auditory-aging','noise-induced-hearing-loss','cochlear-synaptopathy','tinnitus','audiometric-calibration','pure-tone-audiometry','speech-audiometry','acoustic-immittance-tympanometry','otoacoustic-emissions','auditory-evoked-potential','auditory-brainstem-response','speech-intelligibility','speech-reception-threshold','zodiac-in-noise'] },
  { id:'technology',title:'助听器、人工耳蜗与声音编码',english:'Hearing technology',description:'从声学与电接口出发，比较处方目标、增益、动态范围、声音体验、临床编码、通道和时域策略。',slugs:['hearing-aid','hearing-aid-prescription','real-ear-measurement','dynamic-range','cochlear-implant','cochlear-implant-sound-perception','music-perception','cochlear-implant-coding-strategies','channel-interaction','n-of-m-coding','temporal-limits-encoder','f0-in-tfs'] },
  { id:'methods',title:'行为测量、神经记录与研究模型',english:'Methods & models',description:'从心理声学的实验逻辑进入行为测量，再区分神经记录、声学模拟和分析工具，检查验证与推广范围。',slugs:['phonetics','spectrogram','psychoacoustics','auditory-illusion','auditory-computational-models','electroencephalography','neural-speech-tracking','vocoder','get-vocoder','atomic-speech-model','speech-reception-threshold','confusion-matrix','signal-detection-theory'] },
  { id:'people-history',title:'从研究人物回顾听觉科学',english:'People & research history',description:'从梁之安、江渊声、李量、顾瑞、赵元任、邹路得、刘半农、吴宗济、林焘、马大猷、张家騄、魏荣爵、王季卿、赫尔曼·冯·亥姆霍兹、威廉·豪斯、曼弗雷德·施罗德 、简斯·布劳尔特 、哈维·弗莱彻 、阿尔伯特·布雷格曼 、Lloyd Jeffress 、Bertrand Delgutte 、James L. Flanagan 与 埃伯哈德·茨维克尔 的工作，回顾听觉生理、语音感知、临床测量、汉语语音、生理声学、听觉植入、房间声学、语音编码、空间听觉、听觉测量、知觉组织与双耳机制研究。',slugs:['liang-zhian','nelson-kiang','li-liang','gu-rui','zhao-yuanren','zou-lude','liu-bannong','wu-zongji','lin-tao','ma-dayou','zhang-jialu','wei-rongjue','wang-jiqing','hermann-von-helmholtz','william-f-house','manfred-r-schroeder','jens-blauert','harvey-fletcher','albert-bregman','lloyd-jeffress','bertrand-delgutte','james-l-flanagan','eberhard-zwicker'] },
];

export const allLearningPaths = [
  ...introductoryPaths.map(path => ({ ...path, slugs: path.steps.map(step => step.slug) })),
  ...learningPaths,
];
