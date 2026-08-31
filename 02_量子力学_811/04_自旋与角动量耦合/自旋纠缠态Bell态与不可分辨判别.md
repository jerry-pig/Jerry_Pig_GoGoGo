# 自旋纠缠态（Bell 态）与不可因式分解判别

> **图谱所属**：[[00_量子物理模型图谱_MOC]]  
> **考纲定位**：811 量子力学 · 自旋（大纲明确要求了解）  
> **掌握度**：🟩 能够判定两粒子波函数是否为纠缠态

---

## 🌌 1. 物理情景与 Bell 态定义

对于两个自旋为 $1/2$ 的全同（或非全同）粒子系统，其组合自旋空间由四个正交归一的基矢（**Bell 态**）构成：

### 1.  singlet（自旋单态，$S=0$）
$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}} ( |\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle )
$$
- 这是具有**反对称性**的纠缠态，总自旋 $S=0$，总磁量子数 $M_s=0$。

### 2. triplet（自旋三重态，$S=1$）
- $M_s = 1$：
  $$
  |\Phi^+\rangle = \frac{1}{\sqrt{2}} ( |\uparrow\uparrow\rangle + |\downarrow\downarrow\rangle )
  $$
- $M_s = -1$：
  $$
  |\Phi^-\rangle = \frac{1}{\sqrt{2}} ( |\uparrow\uparrow\rangle - |\downarrow\downarrow\rangle )
  $$
- $M_s = 0$：
  $$
  |\Psi^+\rangle = \frac{1}{\sqrt{2}} ( |\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle )
  $$
  三重态在自旋交换下是**对称**的。

---

## ⚡ 2. 纠缠态的数学判定（不可因式分解性）

定义一个双粒子纯态为：
$$
|\psi\rangle = a |\uparrow\uparrow\rangle + b |\uparrow\downarrow\rangle + c |\downarrow\uparrow\rangle + d |\downarrow\downarrow\rangle
$$

### 1. 可分离态（Separable State）的条件
如果该状态可以写成两个独立单粒子状态的直积形式：
$$
|\psi\rangle = |\psi_1\rangle \otimes |\psi_2\rangle = (\alpha_1 |\uparrow\rangle + \beta_1 |\downarrow\rangle) \otimes (\alpha_2 |\uparrow\rangle + \beta_2 |\downarrow\rangle)
$$
对应系数展开为：
$$
a = \alpha_1\alpha_2, \quad b = \alpha_1\beta_2, \quad c = \beta_1\alpha_2, \quad d = \beta_1\beta_2
$$
可得判定恒等式：
$$
ad - bc = \alpha_1\alpha_2\beta_1\beta_2 - \alpha_1\beta_2\beta_1\alpha_2 = 0
$$

### 2. 纠缠态（Entangled State）的判定条件
若 **$ad - bc \neq 0$**，则该状态无法因式分解，为**纠缠态**。
- 以单态 $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$ 为例：
  $a=0, b=\frac{1}{\sqrt{2}}, c=-\frac{1}{\sqrt{2}}, d=0 \implies ad-bc = \frac{1}{2} \neq 0$，故为**最大纠缠态**。

---

## 🔬 3. 物理图像与测量坍缩

- **非定域性（EPR佯谬）**：若两粒子处于单态 $|\Psi^-\rangle$，在空间上将它们拉开到无穷远。
  - 若测量粒子 1 的自旋，得到 $|\uparrow\rangle$（概率 50%）；
  - 此时，即使相隔光年，粒子 2 的状态会瞬时坍缩为 $|\downarrow\rangle$，表现出强大的量子关联。

---

## 🕳️ 4. 避坑手记
- **自旋对称性与费曼单态的联系**：在全同费米子（如两个电子）构成的体系中，总波函数必须是反对称的。
  - 若空间波函数对称，则自旋波函数必须是反对称的（即自旋单态 $|\Psi^-\rangle$）；
  - 若空间波函数反对称，则自旋波函数必须是对称的（即自旋三重态之一）。
  - 这是一级微扰计算（如氦原子的交换积分项）的前置步骤，必须分清。
- 关联卡片：[[自旋轨道耦合精细结构与超精细结构]]；[[氦原子变分法基态能量近似]]
