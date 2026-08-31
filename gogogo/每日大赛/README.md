# 每日大赛 (Daily Tournament) · 理论物理考研每日训练中枢

> **版本**：v4.0（EB Garamond 典雅学术版 · 认知心流系统）  
> **适用目标**：2027 届中国科学院大学 (UCAS) / 杭州高等研究院 (杭高院) 理论物理专业（604 高等数学 + 811 量子力学）

---

## 一、 设计哲学与运作机制

「每日大赛」是一套**兼具学术典雅质感、心流驱动与现代认知科学学习机制的每日作战系统**。

每天一份独立的 `YYYY-MM-DD/每日大赛.tex`，并通过 XeLaTeX 编译为高清 5 页 PDF。它严格遵循**心流推进五部曲与认知学徒制**：

1. **Page 1: COVER（典雅学术封面）** —— 抽象相空间动量/能量轴与波函数艺术几何，直标 604 & 811 当日模块、五因协议与双轨目标（标准 5.5–6.5h vs 保底 3.5h）。
2. **Page 2: §1 TACTICAL BRIEFING & WARM-UP RETRIEVAL（任务简报与白纸破冰）** —— 5–10 分钟极低启动阻力，不看笔记默写 3 个核心公式/定义，跨越启动能垒。
3. **Page 3: §2 CORE PROBLEM SET（核心战役）** —— 
   - **M1（604 高数）**：一题完整规范书写（微积分或线性代数，建议用时 20–30 min）；
   - **Q1（811 量力）**：一题完整物理推导与算符代数（建议用时 30–45 min）；
   - **Extension（思考与拓展）**：可选概念深度辨析（$\le 10$ min）；
   - 独立作答合计限时 $\le 80$ 分钟，杜绝题海战术，强调手推到最后一步。
4. **Page 4: §3 MODEL SOLUTIONS & COMMENTARY（参考解析与名师评注）** —— 独立成页（防剧透），包含 Strategy（突破口）、Derivation（标准步骤）、Common Error（避坑）与 Checkpoints（量纲与自检）。
5. **Page 5: §4 DAILY DEBRIEF & REFLECTION（战报复盘与反思）** —— 睡前 5 分钟填写，量化耗时、作答状态、5 大错因归因，自动将卡点排入 3 天后的提取重做。

---

## 二、 目录架构

```
每日大赛/
├── README.md                          # 本说明手册
├── 大纲/
│   └── 2027国科大杭高院理论物理_备考总纲.tex/pdf # 唯一权威 16 周推进总纲
├── template/
│   ├── 每日大赛_模板.tex              # 锁定主模板 (EB Garamond + 华文楷体)
│   ├── 每日大赛_模板.pdf              # 模板编译预览版
│   └── 每日大赛生成规范与AI指引.md     # 供 AI 调用的标准化生成与编译规范
└── YYYY-MM-DD/                        # 每日独立实战文件夹（如 2026-08-31/）
    ├── 每日大赛.tex                    # 当日 TeX 源码
    └── 每日大赛.pdf                    # 编译成品的 5 页高清 PDF
```

---

## 三、 标准编译与清理指令

进入对应日期文件夹后，执行 XeLaTeX 双编译以保证页码引用与 `LastPage` 准确：

```powershell
cd "d:\Notebook\Product_Note\gogogo\每日大赛\YYYY-MM-DD"
xelatex -interaction=nonstopmode -halt-on-error 每日大赛.tex
xelatex -interaction=nonstopmode -halt-on-error 每日大赛.tex
Remove-Item -Path "*.aux", "*.log", "*.out", "*.toc" -ErrorAction SilentlyContinue
```

> **目录纯洁性原则**：每个日期文件夹中只保留 `每日大赛.tex`、`每日大赛.pdf` 以及后续归档的 `手写/` 答题扫描图，编译产生的临时缓存一律自动清除。
