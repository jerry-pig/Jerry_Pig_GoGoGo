# ⚡ 算符指数对易子与 BCH 展开（平移生成元）

> **图谱所属**：[[00_量子物理模型图谱_MOC]]  
> **考纲归属**：**超纲高危**（官方大纲未提及，但 2019/2020/2022 年均已出题）  
> **危险等级**：🔴 极高（3次历年题）  
> **底层工具**：Operator Algebra — 算符代数进阶定理

---

## 📌 1. 三个核心恒等式

### 恒等式 A：$[\hat{A}, e^{\hat{B}}]$（2022年考法）
若 $[\hat{A}, \hat{B}] = C$（C 为常数），则：
$$
\boxed{[\hat{A}, e^{\hat{B}}] = C\, e^{\hat{B}}}
$$

**推导路线**（展开幂级数逐项计算）：
$$
e^{\hat{B}} = \sum_{n=0}^\infty \frac{\hat{B}^n}{n!}, \quad [\hat{A}, \hat{B}^n] = n C \hat{B}^{n-1}
$$
因此：
$$
[\hat{A}, e^{\hat{B}}] = \sum_{n=1}^\infty \frac{nC\hat{B}^{n-1}}{n!} = C\sum_{n=1}^\infty \frac{\hat{B}^{n-1}}{(n-1)!} = C e^{\hat{B}} \quad \checkmark
$$

---

### 恒等式 B：Baker-Campbell-Hausdorff (BCH) 公式（平移算符应用）
$$
\boxed{e^{\hat{A}}\hat{B}e^{-\hat{A}} = \hat{B} + [\hat{A}, \hat{B}] + \frac{1}{2!}[\hat{A}, [\hat{A}, \hat{B}]] + \frac{1}{3!}[\hat{A}, [\hat{A}, [\hat{A}, \hat{B}]]] + \cdots}
$$

**特殊情形（链式对易截断）**：若 $[\hat{A}, [\hat{A}, \hat{B}]] = 0$，则：
$$
e^{\hat{A}}\hat{B}e^{-\hat{A}} = \hat{B} + [\hat{A}, \hat{B}]
$$

---

### 恒等式 C：平移算符 $\hat{T}(\alpha) = e^{i\alpha\hat{p}/\hbar}$ 的性质（2020年考法）

$$
\hat{T}(\alpha) = e^{i\alpha\hat{p}/\hbar}
$$
- **位置算符的平移**：
$$
\hat{T}(\alpha)\hat{x}\hat{T}^\dagger(\alpha) = e^{i\alpha\hat{p}/\hbar}\hat{x}e^{-i\alpha\hat{p}/\hbar} = \hat{x} + \alpha
$$
  **推导**（BCH 展开，令 $\hat{A} = i\alpha\hat{p}/\hbar$，利用 $[\hat{x}, \hat{p}] = i\hbar$）：
$$
[i\alpha\hat{p}/\hbar, \hat{x}] = i\alpha/\hbar \cdot (-i\hbar) = \alpha \quad \text{（截断！因为 }\hat{p}\text{ 与常数对易）}
$$

- **动量本征态的作用**：
$$
\langle x'|e^{i\alpha\hat{p}/\hbar} = \langle x' + \alpha|, \quad e^{i\alpha\hat{p}/\hbar}|x'\rangle = |x' - \alpha\rangle
$$

---

## 🛠️ 2. 历年真题对应手推模板

### 2022年第一题：$[\hat{A}, e^{\hat{B}}]$ 的计算与 Hermitian 判断
- 用恒等式 A：若 $[\hat{A}, \hat{B}] = C$（常数），则 $[\hat{A}, e^{\hat{B}}] = Ce^{\hat{B}}$；
- $e^{\hat{B}}$ 为 Hermitian 当且仅当 $\hat{B}$ 是反 Hermitian 算符（$\hat{B}^\dagger = -\hat{B}$）；
- 若 $\hat{B}$ 为 Hermitian，则 $e^{\hat{B}}$ 不是 Hermitian，但 $e^{i\hat{B}}$ 是幺正算符（Unitary）。

### 2019年第三题：证明 $e^{-i\lambda\hat{L}_y} = 1 - i\hat{L}_y\sin\lambda - (1-\cos\lambda)\hat{L}_y^2$（$l=1$ 子空间）
- 先证 $\hat{L}_y^3 = \hat{L}_y$（在 $l=1$ 子空间中，对 $3\times 3$ 矩阵直接计算）；
- 展开 $e^{-i\lambda\hat{L}_y} = \sum_n \frac{(-i\lambda)^n \hat{L}_y^n}{n!}$，利用 $\hat{L}_y^{2k+1} = \hat{L}_y$、$\hat{L}_y^{2k} = \hat{L}_y^2$（$k\geq 1$）分类收项即得。

---

## 🕳️ 3. 避坑手记
- 恒等式 A 成立的**前提是 $[\hat{A},\hat{B}]$ 为 c-数（普通数，非算符）**！如果对易子仍是算符，展开项不截断，需写出完整的 BCH 展开式。
- 平移算符 $e^{i\alpha\hat{p}/\hbar}$ 在物理学中是**动量生成元**；$e^{-i\alpha\hat{x}/\hbar}$ 是**位置生成元**（产生动量移位）。
