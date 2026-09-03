# Python 学习环境框架 v1.0

## 1. 核心理念

把 Plastic 的 changeset（CS 号）作为**学习内容的快照索引**。

每个 CS 不是一个传统意义上的"版本"，而是一个**学习节点**——一段可运行的代码 + 对应笔记 + CodeBuddy 的解读。通过 CS 号，可以随时切回到任意学习状态，反复观察、修改、理解。

## 2. 组件角色

| 组件 | 角色 | 在这个框架里负责什么 |
|------|------|---------------------|
| VSCode | 编辑器 / 运行器 | 写 Python、运行代码、调试、看终端输出 |
| Python | 执行引擎 | 实际运行例程，生成结果和反馈 |
| CodeBuddy | AI 技术搭档 | 生成例程、解释代码、总结规律、回答问题 |
| Plastic SCM | 本地节点索引 | 用 CS 号标记每个学习节点，支持快速切换 |
| Gitee | 远程备份 / 同步 | 把学习代码推到云端，实现多设备访问 |
| IMA 笔记 | 知识沉淀 | 记录概念、CS 号索引、学习总结和问题导向 |

## 3. 数据流

### 正向学习流

```
IMA 笔记定主题
        ↓
CodeBuddy 生成例程
        ↓
VSCode 编写 / 运行 / 调试
        ↓
Plastic 提交为新的 CS
        ↓
Gitee 推送远程备份
        ↓
IMA 更新 CS 索引
```

### 反向回溯流

```
IMA 笔记中查到 CS 号
        ↓
Plastic 切换到该 CS
        ↓
VSCode 查看 / 运行当时的代码
        ↓
CodeBuddy 解释该节点内容
        ↓
继续扩展或返回当前
```

## 4. 目录结构

```
repository/
├── docs/
│   ├── learning-framework.md   # 本框架文档
│   ├── cs-index.md             # CS 号索引表
│   └── topic-map.md            # 主题地图（可选）
├── src/
│   ├── basics/                 # 基础语法
│   ├── stdlib/                 # 标准库
│   ├── algorithms/             # 算法练习
│   └── projects/               # 小项目
├── notes/
│   └── codebuddy-q.md          # 向 CodeBuddy 提问的记录模板
├── README.md
└── .plastic/
```

## 5. 命名约定

### Changeset 注释规范

```
[主题] 简短描述 | 关键字
```

示例：

- `[basics] 变量与数据类型 | var-types`
- `[stdlib] os.path 常用操作 | os-path`
- `[algo] 二分查找实现 | binary-search`

### CS 号索引表格式

见 `cs-index.md`，每行记录：

| CS | 日期 | 主题 | 关键词 | 笔记链接 | 状态 |
|----|------|------|--------|----------|------|
| 1 | 2026-09-03 | 项目初始化 | init | - | done |
| 2 | 2026-09-03 | 变量与数据类型 | var-types | ima://xxx | done |

### 文件命名

- 例程：`src/basics/01_variables.py`
- 笔记片段：`notes/01_variables_notes.md`

## 6. 标准操作流程（SOP）

### 学习一个新主题

1. 在 IMA 笔记中写下主题、目标和已有疑问。
2. 让 CodeBuddy 生成入门例程（说明目标和学习级别）。
3. 在 VSCode 中创建文件并运行，观察输出。
4. 修改参数、打断点、提问，反复验证。
5. 满意后在 Plastic 提交：`cm checkin -c "[主题] 描述 | 关键词"`
6. 记录生成的 CS 号到 `docs/cs-index.md`。
7. 推送到 Gitee：`cm sync` 或对应 git 命令。
8. 在 IMA 中更新该主题的 CS 索引。

### 回溯到某个学习节点

1. 在 IMA 笔记或 `cs-index.md` 中找到 CS 号。
2. 执行切换命令：`cm update cs:<CS号>`
3. VSCode 会自动刷新，显示当时代码。
4. 运行、复习、扩展理解。
5. 如果要基于此继续学习，建议先开分支，避免破坏主线。

### 向 CodeBuddy 提问的标准格式

不要只说"我不懂"，而是提供上下文：

```
主题：XXXX
CS 号：xxx
文件：src/basics/01_variables.py
问题：这段代码为什么输出 YYY？
目标：我想理解 ZZZ
```

这样 CodeBuddy 可以直接定位到当时的上下文，给出精准回答。

## 7. 扩展建议

- 当 CS 多了以后，用 `cm find` 或 `cm log` 按关键字搜索。
- 定期把 `cs-index.md` 同步到 IMA，形成双向索引。
- 每个主题的最后一个 CS 可以打标签（Label），作为"该主题毕业节点"。
- 复杂的练习可以开分支，保留多种解法，最后合并或保留对比。
