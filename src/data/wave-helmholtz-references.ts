import type { Reference } from './references';

export const waveHelmholtzReferences: Record<string, Reference> = {
  'we-unsw-equation': {
    title: 'The wave equation for sound', authors: 'UNSW Physclips', year: '未标年（2026-10-29 核验）', publication: 'University of New South Wales',
    url: 'https://www.animations.physics.unsw.edu.au/jw/sound-wave-equation.htm', access: 'fulltext',
    supports: '阅读压缩、牛顿定律、声波方程和阻抗相关文字；支持小扰动下压缩性与惯性形成传播、声速与体积模量及密度的联系。正文以压力与速度守恒方程独立推导，未转载原图。',
  },
  'we-demanet-2016': {
    title: 'Waves and Imaging: Class notes, 18.325 (Draft December 20, 2016)', authors: 'Laurent Demanet', year: '2016', publication: 'Massachusetts Institute of Technology',
    url: 'https://math.mit.edu/icg/resources/notes325.pdf', access: 'fulltext',
    supports: '针对性核对第1.2.2节一维行波与达朗贝尔解、第1.2.4节亥姆霍兹方程、格林函数与Sommerfeld条件，以及附录B中心差分和CFL限制。原讲义傅里叶约定对应exp(+ikr)外向核，本站转换为exp(jωt)与exp(−ikr)。非通读全部144页，非系统数学史；初态、能量恒等式、离散色散和算例另以代入及独立计算核对。',
  },
  'we-kwave-3d': {
    title: 'kspaceFirstOrder3D — 3D time-domain simulation of wave propagation', authors: 'k-Wave developers', year: '未标年（2026-10-29 核验）', publication: 'k-Wave official documentation',
    url: 'https://www.k-wave.org/documentation/kspaceFirstOrder3D.php', access: 'documentation',
    supports: '核对公开接口说明的介质、声源与传感器输入、空间变化声速和密度、幂律吸收、非线性选项及PML；未安装或运行k-Wave，本站中心差分教学图不代表其实现。',
  },
  'we-comsol-equations': {
    title: 'Supplement A: Equations', authors: 'COMSOL', year: '未标年（2026-10-29 核验）', publication: 'COMSOL Learning Center',
    url: 'https://www.comsol.com/support/learning-center/article/supplement-a-equations-76561', access: 'documentation',
    supports: '阅读Pressure Acoustics、Solid Mechanics、Thermoviscous Acoustics小节的说明文字，核对时域压力方程与频域亥姆霍兹、域源、等效复介质以及压力—速度—温度耦合的模型范围。网页公式有图片／数学资源，具体符号以独立守恒推导核对；未声称运行软件或验证器件。',
  },
  'he-fenics-theory': {
    title: 'The Helmholtz equation', authors: 'Antonio Baiano Svizzero', year: '2026（页面更新，2026-10-29 核验）', publication: 'The FEniCSx tutorial',
    url: 'https://jsdokken.com/dolfinx-tutorial/chapter2/helmholtz.html', access: 'documentation',
    supports: '阅读PDE、Dirichlet/Neumann/Robin边界和弱形式。明确外法向与e^{jωt}约定；页面将一般源q标为体积速度，其点源写法q=Qδ实际区分分布密度与总量。本站明确q单位s⁻¹、Q单位m³/s，并独立检查源项量纲。',
  },
  'he-dolfinx-demo': {
    title: 'Helmholtz equation — DOLFINx Python demo', authors: 'Samuel Groth; Jørgen S. Dokken', year: '2018–2025（版权标年；2026-10-29 核验）', publication: 'DOLFINx official documentation (main)',
    url: 'https://docs.fenicsproject.org/dolfinx/main/python/demos/demo_helmholtz.html', access: 'documentation',
    supports: '阅读复数弱形式、平面波制造解、混合边界及L2/H1误差计算代码，核对测试函数共轭和高波数污染误差说明。main为可更新文档；未运行DOLFINx，不以接口示例声称模型已获实验验证。',
  },
  'he-bempp-operators': {
    title: 'Green’s Representation Theorem; Boundary Operators for the Helmholtz Equation', authors: 'Timo Betcke; Matthew Scroggs', year: '2020（版权标年；2026-10-29 核验）', publication: 'The Bempp Book',
    url: 'https://bempp.com/handbook/theory/greens_representation.html', access: 'documentation',
    supports: '阅读格林表示与自由空间核，另核对https://bempp.com/handbook/api/boundary_operators.html的亥姆霍兹算子接口。原文核为exp(+ikr)，本站用exp(−ikr)且显式说明转换；原页Δg=k²g的中间式有符号问题，不采纳该式，本站源点外(Δ+k²)G=0由独立求导核对。未运行Bempp。',
  },
  'he-comsol-thermoviscous': {
    title: 'Thermoviscous Acoustics Model (COMSOL 6.4)', authors: 'COMSOL', year: '6.4版（2026-10-29 核验）', publication: 'COMSOL Acoustics Module documentation',
    url: 'https://doc.comsol.com/6.4/doc/com.comsol.help.aco/aco_ug_thermo.09.48.html', access: 'documentation',
    supports: '阅读SLNS模型说明、三组场和波长远大于黏热边界层厚度的假设；支持微声学需考虑损耗以及降阶模型有适用范围。未用其替代完整器件验证。',
  },
  'he-fenics-code': {
    title: 'Implementation — Acoustic Helmholtz equation in a tube', authors: 'Antonio Baiano Svizzero; Jørgen S. Dokken', year: '2026（页面核验）', publication: 'The FEniCSx tutorial',
    url: 'https://jsdokken.com/dolfinx-tutorial/chapter2/helmholtz_code.html', access: 'documentation',
    supports: '阅读管道测试问题、速度与阻抗边界、逐频求解及接收位置声压后处理示例；只将其作为进阶方法入口，未运行该教程，未沿用其中材料数值或无反射表述。本站阻抗管为独立解析例子。',
  },
};
