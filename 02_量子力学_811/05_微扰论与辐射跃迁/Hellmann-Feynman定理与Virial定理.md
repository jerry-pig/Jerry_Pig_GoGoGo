# ⚡ Hellmann-Feynman 定理与 Virial 定理

> **图谱所属**：[[00_量子物理模型图谱_MOC]]  
> **考纲归属**：**超纲高危**（官方大纲完全未提及，但 2016/2023 年已出大题）  
> **危险等级**：🔴 极高（2023年整道30分大题）  
> **参考教材**：曾谨言《量子力学教程》附录；朗道《量子力学》§3

---

## 🌌 1. Hellmann-Feynman 定理（HF 定理）

### 定理陈述
设哈密顿量 $\hat{H}(\lambda)$ 依赖于某个参数 $\lambda$，对应归一化本征态 $|\psi_n(\lambda)\rangle$ 和本征值 $E_n(\lambda)$：
$$
\hat{H}(\lambda)|\psi_n(\lambda)\rangle = E_n(\lambda)|\psi_n(\lambda)\rangle
$$

则：
$$
\boxed{\frac{\partial E_n}{\partial \lambda} = \left\langle \psi_n \left| \frac{\partial \hat{H}}{\partial \lambda} \right| \psi_n \right\rangle}
$$

### 推导骨架（简洁版）
$$
\frac{\partial E_n}{\partial \lambda} = \frac{\partial}{\partial \lambda}\langle\psi_n|\hat{H}|\psi_n\rangle = \left\langle\frac{\partial\psi_n}{\partial\lambda}\right|\hat{H}|\psi_n\rangle + \langle\psi_n|\hat{H}\left|\frac{\partial\psi_n}{\partial\lambda}\right\rangle + \left\langle\psi_n\left|\frac{\partial\hat{H}}{\partial\lambda}\right|\psi_n\right\rangle
$$
前两项利用归一化条件 $\langle\psi_n|\psi_n\rangle = 1$ 对 $\lambda$ 求导后等于 $0$，得证。

---

## 🌌 2. Virial 定理（位力定理）

### 定理陈述（WN 定理形式）

对于势能满足 $V(\mathbf{r})$ 的量子力学体系（定态），有：
$$
\boxed{2\langle T \rangle = \left\langle \mathbf{r} \cdot \nabla V \right\rangle}
$$

等价地，若势能满足幂律 $V \propto r^n$，则 $2\langle T\rangle = n\langle V\rangle$。

### 通过 HF 定理证明 Virial 定理（2023年考法）

令 $\hat{H}(\lambda) = \lambda^2\hat{T} + \hat{V}(\lambda\mathbf{r})$（对坐标整体缩放），利用 $\frac{\partial E}{\partial\lambda}\big|_{\lambda=1}=0$（能量对坐标缩放参数在 $\lambda=1$ 处极值），得到 Virial 定理。

---

## 🛠️ 3. 标准应用模板（2023 年真题完整路线）

### 应用 1：谐振子中的 $\langle T \rangle$ 与 $\langle V \rangle$
- 谐振子 $V = \frac{1}{2}m\omega^2 x^2 \propto x^2$（$n=2$）；
- Virial 定理：$2\langle T\rangle = 2\langle V\rangle \implies \langle T\rangle = \langle V\rangle = \frac{E_n}{2} = \frac{(n+1/2)\hbar\omega}{2}$。

### 应用 2：氢原子 $\langle 1/r\rangle$ 与 $\langle 1/r^2\rangle$（2023年第三大题！）

**求 $\langle 1/r\rangle$**：对 $e^2/(4\pi\varepsilon_0)$ 系数求导，令 $\lambda = e^2/(4\pi\varepsilon_0)$：
$$
\frac{\partial E_n}{\partial\lambda} = \left\langle -\frac{1}{r}\right\rangle \implies \left\langle\frac{1}{r}\right\rangle = -\frac{\partial E_n}{\partial\lambda}
$$
已知 $E_n = -\frac{\mu\lambda^2}{2\hbar^2 n^2}$（其中 $\lambda = ke^2$），故：
$$
\left\langle\frac{1}{r}\right\rangle = \frac{\mu k e^2}{\hbar^2 n^2} = \frac{1}{n^2 a_0} \quad \text{（玻尔半径 } a_0 = \frac{\hbar^2}{\mu k e^2}\text{）}
$$

**求 $\langle 1/r^2\rangle$**：对有效势中的离心项系数 $\sim l(l+1)\hbar^2$ 使用 HF 定理对 $l$ 求导（需将 $l$ 视为连续参数）：
$$
\frac{\partial E_{nl}}{\partial l} = \left\langle\frac{\partial\hat{H}}{\partial l}\right\rangle = \left\langle\frac{(2l+1)\hbar^2}{2\mu r^2}\right\rangle
$$
利用 $E_{nl}$ 对 $l$ 的导数计算出 $\langle 1/r^2\rangle = \frac{1}{l+1/2}\frac{1}{n^3 a_0^2}$。

---

## 🕳️ 4. 避坑手记与关联
- **HF 定理的使用前提**：本征态必须是归一化的，参数 $\lambda$ 的变化必须是连续的。
- **Virial 定理仅适用于定态**：非定态（如叠加态）的期望值随时间振荡，Virial 定理给出的是时间平均意义下的关系。
- 关联每日大赛：当每日大赛出现"求 $\langle 1/r\rangle$、$\langle r^2\rangle$"等矩阵元时，HF定理比直接积分快 10 倍！
