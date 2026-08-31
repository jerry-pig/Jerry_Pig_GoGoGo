# 每日大赛生成规范与 AI 指引 (Daily Tournament AI Guide)

> **版本**：v4.1（锁定版：EB Garamond × Garamond-Math × 华文楷体 · 5页功能化版面）  
> **适用对象**：所有接入本项目的 AI Agent / 自动化脚本  
> **核心职责**：根据备考总纲进度，**复制并填写**锁定主模板，生成指定日期的 `每日大赛.tex`，完成 XeLaTeX 双编译。  
> **锁定声明**：`gogogo/每日大赛/template/每日大赛_模板.tex` 的字体、配色、卡片环境、页眉页脚与分区结构已经定稿。生成每日文件时只替换占位内容，**不得改字体、宏包、颜色或版式骨架**。

---

## 〇、 锁定的风格与字体 (Locked Design)

生成任何日期的每日大赛时，必须原样继承主模板 preamble，不得换成 `ctexart`、`newtxmath`、SimSun、Crimson Pro 或其他组合。

### 1. 字体（不可更改）

| 角色 | 字体 | 说明 |
| :--- | :--- | :--- |
| 拉丁正文 | **EB Garamond**（Regular / Italic / SemiBold） | TeX Live：`ebgaramond`；旧式数字 |
| 页眉等无衬线 | **Libertinus Sans** | `Scale=MatchLowercase` |
| 数学与希腊字母 | **Garamond-Math** | `unicode-math`；与正文同一骨架，禁止 `newtxmath` / `amssymb` |
| 中文正文 | **华文楷体** `STKaiti`（`C:/Windows/Fonts/STKAITI.TTF`） | 仅题目正文与解答正文使用中文 |
| 中文无衬线 / 等宽 | Microsoft YaHei / FangSong | 仅作 CJK 回退，界面标签仍用英文 |

引擎为 **XeLaTeX**。先 `fontspec` + `amsmath` + `unicode-math` 设定拉丁与数学，再加载 `xeCJK`（`CJKmath=false`，`PunctStyle=kaiming`），避免中文包改写主字体。

### 2. 语言分工（不可更改）

- **英文**：封面、页眉页脚、所有分区标题、题卡标题、解答小标题（Strategy / Derivation / Physical Picture 等）、复盘表字段。
- **中文**：仅 **题目正文**（M1 / Q1 / Extension）、**解答正文**（Strategy 等标签之后的叙述与公式说明）以及 **工作区指引文案**。

### 3. 配色与卡片环境（不可更改）

沿用模板中的 TeXtured 色板：`navy` `#0F172A`、`slate` `#1E293B`、`royal` `#1E40AF`、`mist` `#64748B`、`border` `#E2E8F0`、`paper` `#F8FAFC`、`forest` `#065F46`、`amber` `#D97706`、`wine` `#991B1B`、`ice` `#EFF6FF`。

| 环境名 | 用途 |
| :--- | :--- |
| `briefing` | §1 任务简报 + 热身勾选清单 |
| `problem` | §2 题卡（两个参数：标题、建议用时） |
| `solution` | §3 解析卡 |
| `debrief` | §4 复盘表 |
| `notebox` / `warnbox` | 提示条 / 避坑条 |

### 4. 锁定 5 页功能化结构 (Zero Awkward Blank Pages)

完整 PDF = **封面 + 四个大分区，每个分区各自 `\clearpage` 独立成页，且版面功能充实**：

1. **Page 1: Cover**（`titlepage`，无页眉，抽象相图与几何艺术）
2. **Page 2: §1 Tactical Briefing & Warm-Up Retrieval**
   - 包含简报卡片、动量防御线提醒；
   - 包含 **Warm-Up Retrieval Workspace（白纸破冰草稿区，预留手写空间）**，消灭下半页空白。
3. **Page 3: §2 Core Problem Set**（独立测试卷，包含 M1、Q1 与可选 Extension）
4. **Page 4: §3 Model Solutions & Commentary**（独立成页，彻底隔离防剧透）
5. **Page 5: §4 Daily Debrief & Reflection**
   - 包含复盘表格（耗时与 5 大错因勾选）；
   - 包含 **Key Derivation Insights & Traps（核心突破口与避坑沉淀栏，预留三项核心记录）**，消灭下半页空白。

页眉页脚英文：左页眉 `2027 Theoretical Physics · 604 Calculus & 811 Quantum Mechanics`；右页眉 `Daily Tournament · [日期]`；左页脚 `"Calculate until the very last step."`；右页脚 `Page n of LastPage`。

---

## 一、 生成前必读清单 (Pre-flight Checklist)

在为指定日期（如 `YYYY-MM-DD`）生成每日大赛前，**必须严格按顺序读取以下文件**：

1. **总纲与学习系统**：`gogogo/document/specs.md`
   - 根据日期确定当前属于 **第几周（共 16 周）**；
   - 提取当周对应 **604 高等数学主线模块** 与 **811 量子力学主线模块**；
   - 严格遵循 16 周节点递进，严禁跳步。
2. **历史错题与间隔提取**：
   - 检查前 1 天与前 3 天的 `YYYY-MM-DD/每日大赛.tex`（若存在）；
   - 提取前序复盘中的弱项或未掌握点，放入当日 **§1 Warm-Up Retrieval** 或 **§2 Extension**。
3. **主模板（锁定源）**：`gogogo/每日大赛/template/每日大赛_模板.tex`
   - 复制整份模板到 `每日大赛/YYYY-MM-DD/每日大赛.tex`，只替换 `[YYYY-MM-DD]`、`[X]`、`[N]`、`[phase]`、`[module]` 以及题目/解答正文。

---

## 二、 内容编排与出题准则 (Authoring Rules)

### 1. 各区内容细则

- **§1 Briefing**
  - **604**：1 项明确概念/方法 + 指向当日 M1；
  - **811**：1 项经典模型/定理白纸提取 + 指向当日 Q1；
  - **Supporting**：英语 1 篇真题精读/长难句 + 政治对应模块；
  - **Momentum Defence Line**：标准 5.5–6.5 h；低配 3.5 h（必保 811 提取 + M1 + 英语精读）；
  - **Warm-Up Retrieval Checklist**：不看笔记默写 3 个核心公式/定理（勾选框）；
  - **Workspace**：预留白纸盲写推导区。
- **§2 Arena**
  - **M1 (604)**：1 道典型题；题卡标题英文（含题型）；正文中文；建议用时通常 20–30 min；
  - **Q1 (811)**：1 道核心推导；题卡标题英文（含模型）；正文中文；建议用时通常 30–45 min；
  - 主问题合计限时 $\le 80$ min，杜绝题海，手推到最后一步；
  - **Extension**：可选概念辨析或错题微变式，建议 $\le 10$ min。
- **§3 Solutions**（另页）
  - M1：Strategy（突破口）+ Derivation（规范步骤）+ Common Error（避坑）；
  - Q1：Physical Picture（图像与建模）+ Derivation + Checkpoint（边界 / 归一化 / 共轭 / 量纲等）；
  - 小标题保持英文，叙述与公式说明用中文。
- **§4 Debrief**
  - 604 / 811：实际用时、Independent / Used hints / Incomplete、五因勾选；
  - 五因英文标签：Knowledge gap、Modelling、Logic、Calculation、Time；
  - Spaced retrieval in 3 days；当日评估：Peak / Steady / Minimum defence；
  - 下方沉淀栏：写下核心突破口、避坑点与 3 天后提取承诺。

---

## 三、 LaTeX 排版与语法规范 (LaTeX Best Practices)

1. **杜绝 Unicode Emoji**：
   - 严禁在源码中使用表情字符；用 LaTeX 符号或 `[M1]`、`[Q1]`。
2. **数学公式规范**：
   - 行内 `$...$`；独立行 `\[ ... \]`；多行 `\begin{aligned}...\end{aligned}`；
   - 算符与希腊字母走 Garamond-Math（如 $\hat{H}$, $\hbar$, $\psi$）。
3. **断页**：封面之后，§1、§2、§3、§4 均使用 `\clearpage`，与锁定模板一致。

---

## 四、 编译与清理流水线 (Execution Pipeline)

```powershell
cd "d:\Notebook\Product_Note\gogogo\每日大赛\YYYY-MM-DD"
xelatex -interaction=nonstopmode -halt-on-error 每日大赛.tex
xelatex -interaction=nonstopmode -halt-on-error 每日大赛.tex
Remove-Item -Path "*.aux", "*.log", "*.out", "*.toc" -ErrorAction SilentlyContinue
```

日期文件夹只保留 `每日大赛.tex`、`每日大赛.pdf` 及可选的 `手写/` 扫描件。

---

## 五、 标准触发提示词模版 (For Prompt Callers)

当用户说：**“请为我生成 YYYY-MM-DD 的每日大赛”** 时，AI 应自动：
1. 查阅 `document/specs.md` 确定周次与知识点；
2. **复制锁定模板** 为 `gogogo/每日大赛/YYYY-MM-DD/每日大赛.tex`，只填占位，不改字体与版式；
3. 运行上述 PowerShell 指令完成双编译与清理；
4. 输出简短摘要，确认生成成功并提示用户开始作答。
