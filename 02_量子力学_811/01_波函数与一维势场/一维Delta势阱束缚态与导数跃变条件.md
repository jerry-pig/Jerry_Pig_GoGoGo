# 一维 Delta 势阱束缚态与波函数导数跃变匹配条件 (811 核心母题)

> **所属模块**：[[00_量子物理模型图谱_MOC]] ｜ 一维势场定态求解  
> **考纲定位**：811 定态薛定谔方程严格求解、波函数连续性与导数阶跃条件、几率流密度守恒  
> **难度评级**：⭐⭐⭐ ｜ **重要度**：⭐⭐⭐⭐⭐（国科大/中科院极高频基础大题）

---

## 🧭 一、 物理情景与哈密顿量

设一维质量为 $m$ 的粒子在单一吸引型 $\delta$ 势阱中运动：
$$V(x) = -\alpha \delta(x) \quad (\alpha > 0)$$

定态薛定谔方程为：
$$-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} - \alpha \delta(x)\psi(x) = E\psi(x)$$

---

## 🔬 二、 核心断点 1：波函数在奇点处的导数跃变条件推导

当势能包含 Dirac $\delta$ 函数时，势场在 $x=0$ 处无限深发散，此时波函数**本身保持连续**，但其**一阶导数产生有限阶跃**！

### 严格积分推导：
在开区间 $[-\epsilon, +\epsilon]$ 上对定态薛定谔方程两边积分：
$$-\frac{\hbar^2}{2m}\int_{-\epsilon}^{+\epsilon} \psi''(x)\,dx - \alpha \int_{-\epsilon}^{+\epsilon} \delta(x)\psi(x)\,dx = E \int_{-\epsilon}^{+\epsilon} \psi(x)\,dx$$

令 $\epsilon \to 0^+$ 取极限：
1. 第一项：$-\frac{\hbar^2}{2m} [\psi'(0^+) - \psi'(0^-)]$；
2. 第二项：$-\alpha \psi(0)$（利用 $\delta$ 函数的筛选性质）；
3. 右边项：$\lim_{\epsilon \to 0} E \int_{-\epsilon}^{+\epsilon} \psi(x)\,dx = 0$（因为 $\psi(x)$ 有限连续，积分区间长度趋于零）。

由此严格导出**一维 $\delta$ 势场的导数跃变匹配条件**：
$$\Delta \psi'(0) = \psi'(0^+) - \psi'(0^-) = -\frac{2m\alpha}{\hbar^2}\psi(0)$$

---

## 🎯 三、 核心断点 2：束缚态 ($E < 0$) 能量本征值与波函数求解

设束缚态能量 $E = -|E| < 0$，引入衰减波数：
$$\kappa = \frac{\sqrt{2m|E|}}{\hbar} > 0 \implies E = -\frac{\hbar^2\kappa^2}{2m}$$

### 1. 区域波函数解
在 $x \neq 0$ 区域，$V(x) = 0$，薛定谔方程化为 $\psi''(x) = \kappa^2 \psi(x)$：
- 当 $x > 0$ 时，满足 $x\to+\infty$ 波函数有界（平方可积）：$\psi_R(x) = A e^{-\kappa x}$；
- 当 $x < 0$ 时，满足 $x\to-\infty$ 波函数有界：$\psi_L(x) = B e^{\kappa x}$。

### 2. 边界匹配
- **在 $x=0$ 处波函数连续**：$\psi(0^-) = \psi(0^+) \implies B = A$。  
  波函数写为统一形式：$\psi(x) = A e^{-\kappa |x|}$（偶宇称态）。
- **在 $x=0$ 处应用导数跃变条件**：
  $$\psi'(0^+) = -\kappa A, \quad \psi'(0^-) = \kappa A$$
  代入匹配式：
  $$(-\kappa A) - (\kappa A) = -\frac{2m\alpha}{\hbar^2} A \implies -2\kappa A = -\frac{2m\alpha}{\hbar^2} A$$
  由于束缚态非平凡解 $A \neq 0$，立刻解得衰减波数：
  $$\kappa = \frac{m\alpha}{\hbar^2}$$

### 3. 束缚态能级与归一化波函数
- **能量本征值**：
  $$E_0 = -\frac{\hbar^2\kappa^2}{2m} = -\frac{\hbar^2}{2m}\left(\frac{m\alpha}{\hbar^2}\right)^2 = -\frac{m\alpha^2}{2\hbar^2}$$
- **波函数归一化**：
  $$\int_{-\infty}^{+\infty} |\psi(x)|^2\,dx = 2 \int_0^\infty A^2 e^{-2\kappa x}\,dx = 2A^2 \cdot \frac{1}{2\kappa} = \frac{A^2}{\kappa} = 1 \implies A = \sqrt{\kappa} = \frac{\sqrt{m\alpha}}{\hbar}$$
  因此归一化基态波函数为：
  $$\psi_0(x) = \sqrt{\frac{m\alpha}{\hbar^2}}\,e^{-\frac{m\alpha}{\hbar^2}|x|}$$

---

## ❓ 四、 为什么一维 $\delta$ 势阱只有唯一个束缚态？（奇偶宇称分析）

1. **偶宇称态**：上述求解的 $\psi_0(-x) = \psi_0(x)$ 为偶宇称，存在唯一解；
2. **奇宇称态**：若存在奇宇称束缚态，则必须满足 $\psi(0) = 0$。  
   若 $\psi(0) = 0$，则导数跃变条件变为 $\psi'(0^+) - \psi'(0^-) = 0$（导数无跃变，在 $x=0$ 处连续）。  
   但在 $x>0$ 时 $\psi = C e^{-\kappa x}$，奇宇称要求 $x<0$ 时 $\psi = -C e^{\kappa x}$。此时 $\psi'(0^+) = -\kappa C$，$\psi'(0^-) = -\kappa C$，两者相等要求满足微分方程，但在 $x=0$ 点波函数连续性要求 $C = -C \implies C = 0$。  
   故**不存在非零奇宇称束缚态**！
3. **物理结论**：一维单 $\delta$ 势阱**无论势阱多浅（$\alpha$ 多小），永远且仅存在一个偶宇称束缚态**！

---

## 🌊 五、 几率流密度与定态实波函数定理

几率流密度定义为：
$$J(x) = \frac{\hbar}{2mi}\left(\psi^* \frac{d\psi}{dx} - \psi \frac{d\psi^*}{dx}\right) = \frac{\hbar}{m}\operatorname{Im}\left(\psi^* \frac{d\psi}{dx}\right)$$

- **计算上述束缚态的几率流密度**：
  由于 $\psi_0(x) = \sqrt{\kappa}e^{-\kappa |x|}$ 是纯实数函数，$\psi_0^* = \psi_0$。
  $$J(x) = \frac{\hbar}{2mi}\left(\psi_0 \psi_0' - \psi_0 \psi_0'\right) \equiv 0$$
- **普遍物理定理**：
  **任意一维定态束缚态（或无简并定态）的波函数总可以通过提取全局相位化为纯实数，其实波函数的几率流密度在全空间恒等于零（$J \equiv 0$）**。
  - 物理图像：束缚态对应驻波，没有净概率流向无穷远处传输，概率在空间处于静止稳定分布（满足连续性方程 $\frac{\partial \rho}{\partial t} = -\frac{\partial J}{\partial x} = 0$）。
