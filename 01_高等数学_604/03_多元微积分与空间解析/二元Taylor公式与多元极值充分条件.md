# 二元Taylor公式与多元极值充分条件（含Lagrange乘数法）

> **图谱所属**：[[00_高数知识图谱_MOC]]  
> **考纲定位**：604 高等数学 · 多元微分学（二元 Taylor 公式、无条件极值 Hessian 判定、条件极值 Lagrange 乘数法）  
> **掌握度**：🟩 能够利用二阶偏导数行列式判定局部极值，利用 Lagrange 乘数法求解约束条件最值

---

## 📌 1. 核心定理与极值判定法

### 1. 二元 Taylor 展开（二阶形式）
设 $f(x,y)$ 在点 $(x_0, y_0)$ 的某邻域内具有连续的二阶偏导数，记 $h = x - x_0, k = y - y_0$，则：
$$
f(x_0+h, y_0+k) = f(x_0, y_0) + (h f_x + k f_y) + \frac{1}{2!} (h^2 f_{xx} + 2hk f_{xy} + k^2 f_{yy}) + o(h^2+k^2)
$$
写成向量与矩阵形式：
$$
f(X) = f(X_0) + \nabla f(X_0)^T (X-X_0) + \frac{1}{2} (X-X_0)^T H(X_0) (X-X_0) + o(\|X-X_0\|^2)
$$
其中 $H(X_0)$ 是 **Hessian 矩阵**：
$$
H = \begin{pmatrix}
f_{xx} & f_{xy} \\
f_{yx} & f_{yy}
\end{pmatrix} = \begin{pmatrix} A & B \\ B & C \end{pmatrix}
$$

### 2. 无条件极值充分条件（Hessian 判别式法）
设 $(x_0, y_0)$ 是 $f(x,y)$ 的驻点（即 $f_x=0, f_y=0$）。令：
$$
A = f_{xx}(x_0, y_0), \quad B = f_{xy}(x_0, y_0), \quad C = f_{yy}(x_0, y_0)
$$
计算判别式（即 Hessian 矩阵的行列式）：
$$
\Delta = AC - B^2 = \det(H)
$$
- **若 $\Delta > 0$**：函数在此点有极值。
  - **若 $A > 0$**（Hessian 矩阵正定）：为**极小值**；
  - **若 $A < 0$**（Hessian 矩阵负定）：为**极大值**。
- **若 $\Delta < 0$**（Hessian 矩阵不定）：无极值，此点为**鞍点**。
- **若 $\Delta = 0$**：失效，无法判定（需更高阶展开或结合几何分析）。

---

## 🎯 2. 条件极值：拉格朗日乘数法 (Lagrange Multipliers)

### 1. 几何本质（相切原理）
当在约束条件 $\varphi(x, y, z) = 0$ 下求目标函数 $f(x, y, z)$ 的极值时，极值点必然发生在**目标函数的等值面与约束曲面相切的位置**！
相切意味着两者的法向量共线（平行）：
$$
\nabla f = \lambda \nabla \varphi
$$

### 2. 解题标准 3 步法：
1. **构造 Lagrange 辅助函数**：
   $$L(x, y, z, \lambda) = f(x, y, z) - \lambda \varphi(x, y, z)$$
   *(若有多个约束 $\varphi_1=0, \varphi_2=0$，则引入两个乘子：$L = f - \lambda \varphi_1 - \mu \varphi_2$)*
2. **令所有一阶偏导数等于 0 列方程组**：
   $$\begin{cases} L_x = f_x - \lambda \varphi_x = 0 \\ L_y = f_y - \lambda \varphi_y = 0 \\ L_z = f_z - \lambda \varphi_z = 0 \\ L_\lambda = -\varphi(x, y, z) = 0 \end{cases}$$
3. **方程组求解三大秒杀技巧**：
   - **两式相比法**：$\frac{f_x}{\varphi_x} = \frac{f_y}{\varphi_y} = \frac{f_z}{\varphi_z} = \lambda$，直接消去未知的乘子 $\lambda$，建立 $x, y, z$ 的纯几何比例关系；
   - **轮换对称性**：若目标与约束关于变量轮换对称，必有 $x = y = z$；
   - **回代约束**：将变量关系代入约束方程 $\varphi = 0$ 最终定出坐标。

---

## 🛠️ 3. 经典母题与推导骨架

### 【母题 1 · 无条件极值与鞍点判定】
求函数 $f(x,y) = x^3 - y^3 - 3x^2 + 3y^2$ 的所有极值点与鞍点。

**解题骨架**：
1. **求一阶偏导找驻点**：
   $$\begin{cases} f_x = 3x^2 - 6x = 3x(x-2) = 0 \\ f_y = -3y^2 + 6y = -3y(y-2) = 0 \end{cases} \implies \text{驻点：}(0,0), (0,2), (2,0), (2,2)$$
2. **求二阶偏导数**：$f_{xx} = 6x-6, f_{xy} = 0, f_{yy} = -6y+6$。
3. **逐点分析 $\Delta = AC - B^2$**：
   - $(0,0)$：$A=-6, B=0, C=6 \implies \Delta = -36 < 0 \implies$ **鞍点**。
   - $(2,2)$：$A=6, B=0, C=-6 \implies \Delta = -36 < 0 \implies$ **鞍点**。
   - $(2,0)$：$A=6, B=0, C=6 \implies \Delta = 36 > 0$ 且 $A > 0 \implies$ **极小点**，极小值 $f(2,0) = -4$。
   - $(0,2)$：$A=-6, B=0, C=-6 \implies \Delta = 36 > 0$ 且 $A < 0 \implies$ **极大点**，极大值 $f(0,2) = 4$。

---

### 【母题 2 · 双平面交线上的空间条件极值】
求函数 $u = x^2 + y^2 + z^2$ 在平面约束 $x+y+z=1$ 与 $x-y+z=0$ 下的极小值与最近点。

**标准 Lagrange 乘数法求解**：
1. 构造 $L = x^2+y^2+z^2 - \lambda(x+y+z-1) - \mu(x-y+z)$。
2. 求导：
   $$\begin{cases} L_x = 2x - \lambda - \mu = 0 \implies 2x = \lambda + \mu \\ L_y = 2y - \lambda + \mu = 0 \implies 2y = \lambda - \mu \\ L_z = 2z - \lambda - \mu = 0 \implies 2z = \lambda + \mu \end{cases}$$
3. 对称性立得 $2x = 2z \implies x = z$。
4. 两约束相减得 $2y = 1 \implies y = \frac{1}{2}$；相加得 $2(x+z) = 1 \implies x+z = \frac{1}{2} \implies x = z = \frac{1}{4}$。
5. 极小点为 $\mathbf{(\frac{1}{4}, \frac{1}{2}, \frac{1}{4})}$，极小值为 $\mathbf{u_{\min} = \frac{3}{8}}$，空间最近距离为 $\mathbf{d = \frac{\sqrt{6}}{4}}$。

---

## 🕳️ 4. 避坑手记

1. **判别式符号莫混淆**：务必牢记 $\Delta = AC - B^2 = \det(H)$。若记成 $B^2 - AC$ 会把符号完全反转！
2. **$\Delta = 0$ 决不能下结论**：此时 Hessian 矩阵退化（特征值有 0），必须通过取路径（如沿 $y=x$ 与 $y=-x$）判定是否同号。
3. **Lagrange 乘数法不要死解 $\lambda$**：$\lambda$ 只是中间参数，考题并不需要你求 $\lambda$，**第一优先级永远是用两式相除把 $\lambda$ 迅速消去**！
