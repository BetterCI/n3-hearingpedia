import type { Reference } from './references';
export const vibrationsAcousticsReferences: Record<string, Reference> = {
  "va-free": {
    "title": "Constant-coefficient second-order linear ODEs",
    "authors": "Jiří Lebl",
    "year": "在线版；2026-11-02核对",
    "publication": "作者或机构官方教学资料",
    "url": "https://www.jirka.org/diffyqs/html/sec_ccsol.html",
    "access": "fulltext",
    "supports": "质量弹簧阻尼方程、特征根与欠/临界/过阻尼；本文参数、初值和能量另行复算。"
  },
  "va-forced": {
    "title": "Forced oscillations and resonance",
    "authors": "Jiří Lebl",
    "year": "在线版；2026-11-02核对",
    "publication": "作者或机构官方教学资料",
    "url": "https://www.jirka.org/diffyqs/html/forcedo_section.html",
    "access": "fulltext",
    "supports": "强迫响应及位移峰条件；本文明确速度峰、功率和半功率带宽的不同定义。"
  },
  "va-modal": {
    "title": "Recitation 12 Notes: Modal Analysis",
    "authors": "MIT 2.003SC Engineering Dynamics",
    "year": "2011",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/650ea2d4579aa784f6e46044188560b0_MIT2_003SCF11_rec12note1.pdf",
    "access": "fulltext",
    "supports": "质量与刚度、模态分解与正交；本文两质量矩阵、比例阻尼和直接/模态响应另核对。"
  },
  "va-measurement": {
    "title": "Lecture 1: Sound measurement, rms and peak, lumped elements and waves",
    "authors": "MIT 6.551J / HST.714J 课程（讲义未单独署名）",
    "year": "2004",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/c45734e2684a8592c0600120a0b6584c_lec_1_2004.pdf",
    "access": "fulltext",
    "supports": "声压RMS、相位、频谱与集总/分布描述；不从数字采样值自动推声压校准。"
  },
  "va-lumped": {
    "title": "Lecture 7: Circuit descriptions of acoustic elements",
    "authors": "MIT 6.551J / HST.714J 课程（讲义未单独署名）",
    "year": "2004",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/00610bbb35656bb99990aa06a6b78205_lec_7_2004.pdf",
    "access": "fulltext",
    "supports": "声学顺性、惯抗、体积速度与电路类比；面积换算及阻抗单位单独核对。"
  },
  "va-tubes": {
    "title": "Lectures 15–16: Tubes, natural frequencies and dimensional equations",
    "authors": "MIT 6.551J / HST.714J 课程（讲义未单独署名）",
    "year": "2004",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/151f51f2eb85d88e6b68ad173dc5e932_lec_15_16.pdf",
    "access": "fulltext",
    "supports": "管道模态、端点、输入阻抗与近似；理想开口与真实辐射、损耗分开。"
  },
  "va-plane": {
    "title": "Lecture 2: One-dimensional traveling waves",
    "authors": "MIT 6.551J / HST.714J 课程（讲义未单独署名）",
    "year": "2004",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/1149b68a00a45f7c67d4a5c24ed08b51_lec_2_2004.pdf",
    "access": "fulltext",
    "supports": "线性声学方程、双向行波、压力/速度与反射；本文固定e^(iωt)和峰值相量。"
  },
  "va-spherical": {
    "title": "Lecture 3: Spherical waves, near and far field, radiation impedance",
    "authors": "MIT 6.551J / HST.714J 课程（讲义未单独署名）",
    "year": "2004",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/7056ab51d5cb75810bf976ee38ac8f30_lec_3_2004.pdf",
    "access": "fulltext",
    "supports": "球面外向波、反应性与kr；特别保留纯外向球面波净强度仍等于p_rms²/(rho c)这一限定结论。"
  },
  "va-wave-equation": {
    "title": "The wave equation for sound",
    "authors": "Joe Wolfe / UNSW School of Physics",
    "year": "在线版；2026-11-02核对",
    "publication": "UNSW Physclips / Music Acoustics 官方教学资料",
    "url": "https://www.animations.physics.unsw.edu.au/jw/sound-wave-equation.htm",
    "access": "fulltext",
    "supports": "压强、密度与质点运动，线性化、声速和波方程；不将声速当质点速度。"
  },
  "va-intensity": {
    "title": "Acoustic impedance, intensity and power",
    "authors": "Joe Wolfe / UNSW School of Physics",
    "year": "在线版；2026-11-02核对",
    "publication": "UNSW Physclips / Music Acoustics 官方教学资料",
    "url": "https://www.animations.physics.unsw.edu.au/jw/sound-impedance-intensity.htm",
    "access": "fulltext",
    "supports": "声强、复相量与比声阻抗/声阻抗；采用rho=1.2、c=343得411.6，不沿用页中420近似数值。"
  },
  "va-compliance": {
    "title": "Acoustic compliance, inertance and impedance",
    "authors": "Joe Wolfe / UNSW School of Physics",
    "year": "在线版；2026-11-02核对",
    "publication": "UNSW Physclips / Music Acoustics 官方教学资料",
    "url": "https://www.animations.physics.unsw.edu.au/jw/compliance-inertance-impedance.htm",
    "access": "fulltext",
    "supports": "声学集总元件与体积流，几何尺度及低频近似。"
  },
  "va-decibels": {
    "title": "dB: What is a decibel?",
    "authors": "Joe Wolfe / UNSW School of Physics",
    "year": "在线版；2026-11-02核对",
    "publication": "UNSW Physclips / Music Acoustics 官方教学资料",
    "url": "https://phys.unsw.edu.au/jw/dB.html",
    "access": "fulltext",
    "supports": "功率10log、幅度20log和参考值；本文另明确相关声压叠加和SPL/强度级并非恒等。"
  },
  "va-pipes": {
    "title": "Open vs closed pipes",
    "authors": "Joe Wolfe / UNSW School of Physics",
    "year": "在线版；2026-11-02核对",
    "publication": "UNSW Physclips / Music Acoustics 官方教学资料",
    "url": "https://phys.unsw.edu.au/jw/flutes.v.clarinets.html",
    "access": "fulltext",
    "supports": "压力与位移边界、开开和闭开管谐振；理想边界与端修正分开。"
  },
  "va-helmholtz": {
    "title": "Helmholtz resonance",
    "authors": "Joe Wolfe / UNSW School of Physics",
    "year": "在线版；2026-11-02核对",
    "publication": "UNSW Physclips / Music Acoustics 官方教学资料",
    "url": "https://phys.unsw.edu.au/jw/Helmholtz.html",
    "access": "fulltext",
    "supports": "气颈惯性与腔体顺性、波长远大于尺度与有效颈长；不从无损模型推吸声。"
  },
  "va-ir": {
    "title": "Impulse Responses",
    "authors": "Room EQ Wizard",
    "year": "在线版；2026-11-02核对",
    "publication": "REW 官方帮助",
    "url": "https://www.roomeqwizard.com/help/help_en-GB/html/impulseresponse.html",
    "access": "documentation",
    "supports": "脉冲响应、直达/反射和时窗；本文两抽头例为指定数字模型，未运行REW或测量房间。"
  },
  "va-eigh": {
    "title": "scipy.linalg.eigh",
    "authors": "SciPy developers",
    "year": "在线版；2026-11-02核对",
    "publication": "SciPy 官方接口文档",
    "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh.html",
    "access": "documentation",
    "supports": "实对称广义特征值问题、正定质量矩阵和质量归一化；运行环境SciPy1.17.1。"
  },
  "va-ivp": {
    "title": "scipy.integrate.solve_ivp",
    "authors": "SciPy developers",
    "year": "在线版；2026-11-02核对",
    "publication": "SciPy 官方接口文档",
    "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html",
    "access": "documentation",
    "supports": "积分容差、t_eval和内部步长；本篇积分交叉检查不当严格全局误差保证。"
  },
  "va-diffraction": {
    "title": "Diffraction, shadows, beams, Huygens construction",
    "authors": "Joe Wolfe / UNSW School of Physics",
    "year": "在线版；2026-11-02核对",
    "publication": "UNSW Physclips 官方教学资料",
    "url": "https://www.animations.physics.unsw.edu.au/jw/light/diffraction-shadows-beams-huygens.html",
    "access": "fulltext",
    "supports": "开口与波长尺度的定性绕射；未用光学演示拟合听觉头影、屏障衰减或方向图。"
  }
};
