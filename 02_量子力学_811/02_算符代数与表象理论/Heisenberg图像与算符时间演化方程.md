# Heisenberg 图像与算符时间演化方程

> **图谱所属**：[[00_量子物理模型图谱_MOC]]  
> **考纲定位**：811 量子力学 · 算符理论与图像（大纲明确要求）  
> **掌握度**：🟩 能够写出运动方程并完成平移/演化算符化简

---

## 🌌 1. 物理情景与绘景对比

量子力学有两种完全等价的物理图像（绘景），描述状态随时间的演化方式：

### 1. Schrödinger（薛定谔）图像
- **状态矢量** $|\psi_S(t)\rangle$ 随时间演化，满足含时薛定谔方程：
  $$
  i\hbar \frac{d}{dt} |\psi_S(t)\rangle = \hat{H} |\psi_S(t)\rangle \implies |\psi_S(t)\rangle = \hat{U}(t) |\psi_S(0)\rangle
  $$
  其中时间演化算符 $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$（当 $\hat{H}$ 不含时）。
- **基本力学量算符** $\hat{A}_S$ 不随时间变化（除非算符显含时间，如随时间变化的外场）。

### 2. Heisenberg（海森堡）图像
- **状态矢量** $|\psi_H\rangle$ **恒定不变**，取为 $t=0$ 时刻的状态：$|\psi_H\rangle = |\psi_S(0)\rangle$。
- **力学量算符** $\hat{A}_H(t)$ 随时间演化：
  $$
  \hat{A}_H(t) = \hat{U}^\dagger(t) \hat{A}_S \hat{U}(t) = e^{i\hat{H}t/\hbar} \hat{A}_S e^{-i\hat{H}t/\hbar}
  $$

---

## ⚡ 2. 核心代数与运动方程

### 1. Heisenberg 运动方程（Heisenberg Equation of Motion）
对算符 $\hat{A}_H(t)$ 关于时间求导，可得：
$$
\boxed{\frac{d\hat{A}_H(t)}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{A}_H] + \left( \frac{\partial\hat{A}}{\partial t} \right)_H}
$$
其中最后一项仅在算符显含时间（即 $\frac{\partial \hat{A}_S}{\partial t} \neq 0$）时存在。

### 2. 与经典力学的类比（狄拉克量子化）
对比经典哈密顿力学的正则方程 $\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}$，可见量子力学用对易子** $\frac{i}{\hbar}[\hat{H}, \hat{A}]$** 替换了经典泊松括号 $\{f, H\}$。

---

## 🔬 3. 物理期望等价性与 Ehrenfest 定理

### 1. 期望值不变性
实验可观测物理量是算符的期望值。两种图像计算的期望值完全相同：
$$
\langle A \rangle_t = \langle\psi_S(t)|\hat{A}_S|\psi_S(t)\rangle = \langle\psi_S(0)|\hat{U}^\dagger(t) \hat{A}_S \hat{U}(t)|\psi_S(0)\rangle = \langle\psi_H|\hat{A}_H(t)|\psi_H\rangle
$$

### 2. 埃伦费斯特定理（Ehrenfest's Theorem）
对 Heisenberg 运动方程求期望值，直接得到 Ehrenfest 定理：
$$
\frac{d}{dt} \langle \hat{A} \rangle = \frac{i}{\hbar} \langle [\hat{H}, \hat{A}] \rangle + \left\langle \frac{\partial\hat{A}}{\partial t} \right\rangle
$$
这表明量子力学期望值演化规律与经典力学方程形式完全一致（如 $\frac{d}{dt}\langle x \rangle = \frac{\langle p \rangle}{m}$，$\frac{d}{dt}\langle p \rangle = -\langle \nabla V \rangle$）。

---

## 🕳️ 4. 避坑手记与真题连线
- **守恒量的判定**：若算符不显含时，且与哈密顿量对易 $[\hat{H}, \hat{A}] = 0$，则 $\frac{d\hat{A}_H}{dt} = 0$，力学量 $\hat{A}$ 为**守恒量**。其本征态不随时间演化而发生向其他本征态的跃迁。
- **平移算符的等价形式**：在 2020 年真题第二题中，平移算符作用 $e^{i\alpha\hat{p}/\hbar}\hat{x}e^{-i\alpha\hat{p}/\hbar} = \hat{x} + \alpha$ 在数学形式上与以 $\hat{p}$ 为哈密顿量的 Heisenberg 演化完全同构。
- 关联卡片：[[算符指数对易子与BCH展开_平移生成元]]；[[Hellmann-Feynman定理与Virial定理]]
