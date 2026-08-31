# Bernoulli 方程与全微分方程解法

> **图谱所属**：[[00_高数知识图谱_MOC]]  
> **考纲定位**：604 高等数学 · 常微分方程（大纲明确列出）  
> **认知掌握度**：🟩 闭卷识别类型并独立求解

---

## 📌 一、Bernoulli（伯努利）方程

### 方程形式识别
$$
y' + P(x)y = Q(x)y^n \quad (n \neq 0, 1)
$$

### 换元策略（固定三步）
1. **令** $z = y^{1-n}$；
2. **化简**：$z' = (1-n)y^{-n}y'$，代入原方程：
$$
\frac{z'}{1-n} + P(x)z^{\frac{1}{1-n}} = Q(x)z^{\frac{n}{1-n}}
$$
化简后得**一阶线性方程**：
$$
z' + (1-n)P(x)z = (1-n)Q(x)
$$
3. **用常数变易法求解**一阶线性方程后，代回 $y = z^{1/(1-n)}$。

### 典型例题
$$
y' - \frac{2y}{x} = x^2 y^3 \quad (n=3)
$$
令 $z = y^{-2}$，$z' = -2y^{-3}y'$，代入得：
$$
z' + \frac{4}{x}z = -2x^2
$$
这是关于 $z$ 的一阶线性方程，积分因子 $\mu = e^{\int 4/x\,dx} = x^4$，解得 $z = C/x^4 - x^3/3$，再回代。

---

## 📌 二、全微分方程

### 方程形式识别
$$
M(x,y)\,dx + N(x,y)\,dy = 0
$$
**判断是全微分的充要条件**（区域单连通时）：
$$
\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}
$$

### 求原函数（势函数）三方法

**方法 A：线积分法（最通用）**
$$
u(x,y) = \int_{x_0}^x M(t, y_0)\,dt + \int_{y_0}^y N(x,t)\,dt
$$

**方法 B：凑微分法（速度最快）**
- 观察 $M\,dx + N\,dy$ 中是否包含 $d(xy)$、$d(x^2+y^2)$、$d(x/y)$、$d(\arctan(y/x))$ 等标准全微分形式。

**方法 C：分项组合法**
- 把 $M\,dx$ 中对 $x$ 积分得到 $f(x,y)$，再令 $\partial f/\partial y = N$ 确定积分常数函数 $g(y)$。

### 典型例题
$$
(x^2 + y)\,dx + (x + y^2)\,dy = 0
$$
- 验证：$\partial M/\partial y = 1 = \partial N/\partial x$，是全微分方程；
- 原函数：$u = x^3/3 + xy + y^3/3 = C$。

---

## 🕳️ 3. 避坑手记
- **Bernoulli 方程中 $y=0$ 需单独验证**是否也是解（当 $n>0$ 时 $y=0$ 恒满足）；
- **全微分方程的积分因子**：若 $\partial M/\partial y \neq \partial N/\partial x$，但 $\frac{1}{N}\left(\frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}\right) = \phi(x)$ 只含 $x$，则积分因子 $\mu = e^{\int\phi(x)dx}$ 可将其化为全微分方程。
