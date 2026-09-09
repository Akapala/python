# Python 自学仓库

> 系统自学 Python 的练习仓库。每个板块 = 一份可运行代码 + 一份深度笔记 + 一份教程原文。
> 配套资料在 `D:\workspace\python\work_output\docs/`（CS 索引、审核文档深度笔记、学习框架）。
>
> **当前进度**：入门 1 + 三大板块（turtle / functions / datastructures）共 22 个 .py 文件已完成。

## 环境

| 项 | 版本 |
|---|---|
| Python | 3.12.4 |
| GUI 绑定 | tkinter 8.6（turtle 用） |
| 编辑器 | VSCode + Python 扩展 |
| 版本管理 | Plastic SCM（本地） → GitHub（远程，已从 Gitee 切出） |
| 类型检查 | 已通过 `.vscode/settings.json` 关闭 Pylance 严格模式（贪吃蛇动态属性需要） |

## 目录约定

| 目录 | 用途 |
|---|---|
| `src/` | 代码，一板块一子目录（`01_xxx.py` 编号） |
| `notes/` | 教学笔记，一板块一 md（讲解 + C/C++ 对照 + 调试收获） |
| `docs/` | 教程原文（课件原文，未做修改） |
| `.vscode/` | 本仓库 VSCode 配置（settings.json） |
| `.plastic/` | Plastic SCM workspace 元数据 |

逐行细节写代码注释、体系讲解写笔记、原始教程原文放 docs——**三层不重复维护**。

---

## 学习进度

| # | 板块 | 状态 | 代码目录 | 笔记 | 课数 |
|:---:|---|:---:|---|---|:---:|
| 0 | 入门演练 · 跑马灯 | ✅ 完成 | [`src/hello_world.py`](src/hello_world.py) | [`notes/control-flow.md`](notes/control-flow.md) | 1 |
| 1 | turtle 图形编程 | ✅ 完成 | [`src/turtle/`](src/turtle/) | [`notes/turtle.md`](notes/turtle.md) + [`notes/turtle-takeaways.md`](notes/turtle-takeaways.md) | 9 |
| 2 | 函数与模块 | ✅ 完成 | [`src/functions/`](src/functions/) | [`notes/functions.md`](notes/functions.md) | 6 |
| 3 | 字符串与数据结构 | ✅ 完成 | [`src/datastructures/`](src/datastructures/) | [`notes/datastructures.md`](notes/datastructures.md) | 7 |
| — | `basics/` | 🔧 预留 | `src/basics/`（空目录） | — | — |
| 4 | 文件读写 | 🔜 计划中 | —— | —— | —— |
| 5 | 类与面向对象 | 🔜 计划中 | —— | —— | —— |
| 6 | 异常处理 | 🔜 计划中 | —— | —— | —— |

状态图例：✅ 完成 / 🔧 预留（占位但未启用）/ 🔜 计划中 / 🔄 进行中。

### 三大已完成板块速览

#### 0. 入门演练 `hello_world.py`
第一份代码，跑马灯（清屏 + 字符串切片轮转）。配套笔记 `control-flow.md` 总结 `for/while`、切片、模块导入。

#### 1. turtle 图形编程（9 课）
从画正方形到写贪吃蛇，9 节课覆盖 Python 基础语法 + turtle 全部常用 API：

| 课 | 代码 | 关键技能 |
|:---:|---|---|
| 01 | `01_square.py` | `for range()`、画笔对象 |
| 02 | `02_polygon.py` | `enumerate`、360/n 公式 |
| 03 | `03_color_spiral.py` | 列表、取余 `%`、`tracer/update` |
| 04 | `04_flower.py` | `def` 函数、默认参数、填充 |
| 05 | `05_random_stars.py` | `random` 模块、概率分支 |
| 06 | `06_click_board.py` | 事件回调、闭包、`global` |
| 07 | `07_snowflake.py` | 递归、分形 |
| 08 | `08_snake_game.py` | 综合项目（贪吃蛇） |

#### 2. 函数与模块（6 课）
阶乘 → 默认参数/关键字实参/`*args` → 模块与 `if __name__ == '__main__'` → 作用域 LEGB → 综合练习（gcd/lcm/回文素数）。
**最重要的调试教训**：函数要有兜底 `return`，否则类型检查器会推断成 `int | None`，下游连锁炸。

#### 3. 字符串与数据结构（7 课）
字符串（不可变、切片、格式化）→ 列表（增删排序）→ 推导式 vs 生成器（空间 vs 时间）→ 元组 → 集合（`&`-`|`-`-`-`^`）→ 字典（`get` vs `[]`）→ 综合练习。
**最关键的坑**：`list.sort()` / `list.append()` / `set.add()` 返回 `None`，想拿结果要用 `sorted()`（或干脆不赋值）。

---

## 配套资源（外部）

| 资源 | 位置 | 用途 |
|---|---|---|
| 学习环境框架 | `D:\workspace\python\work_output\docs\learning-framework.md` | 五角色协作 + SOP |
| CS 号索引表 | `D:\workspace\python\work_output\docs\cs-index.md` | 按 Plastic changeset 索引学习节点 |
| 审核文档深度笔记 | `D:\workspace\python\work_output\docs\python-learning-review.md` | 他人提问的深度解析（VSCode 调试 + print） |
| 腾讯文档 `python学习审核` | https://docs.qq.com/doc/DUk9Db3J4Y3JidnV5 | 每日 10:00 自动化巡检，如有新问题会写回深度笔记 |

---

## 版本管理

| 项 | 内容 |
|---|---|
| 本地 | Plastic SCM，`/main` 分支为主学习线 |
| 远程 | GitHub：`https://github.com/Akapala/python.git`（2026-09-09 从 Gitee 迁出 + 重建绑定） |
| 提交格式 | `[板块] 编号 主题 — 核心知识点`（例：`[turtle] 08 贪吃蛇 — 综合项目`） |
| 节奏 | 每完成一课提交一次 |

---

## 调试与工程约定

| 配置 | 位置 | 作用 |
|---|---|---|
| 类型检查 | `.vscode/settings.json` → `"python.analysis.typeCheckingMode": "off"` | 关闭 Pylance，避免贪吃蛇动态属性满屏红线 |
| 教程原文 | `docs/06.函数和模块的使用.md` `docs/07.字符串和常用数据结构.md` | 不修改，仅供笔记对照 |
| `.gitignore`（若改用 Git） | `.vscode/`、`__pycache__/`、`*.pyc` | 工程配置和编译产物不入版本库 |

---

## 注意事项（坑早知道）

| 坑 | 后果 | 规避 |
|---|---|---|
| 文件名 `turtle.py` | 顶掉标准库 `turtle`，`import` 全乱 | 文件夹叫 `turtle` 安全，**文件名绝对不行** |
| `t.ondrag(draw())` | 当场调用一次，注册 `None` | 传函数名，**不加括号** |
| `tracer(0)` 忘了 `update()` | 窗口一片空白 | 配对使用，或干脆删 `tracer(0)` |
| `list.sort()` 赋值给变量 | 拿到 `None`，不是排好序的列表 | 用 `sorted()` 或不赋值 |
| 函数 `for` 循环内 `return` 漏兜底 | 类型推断 `int \| None`，下游连锁炸 | 函数必加兜底 `return` |

---

> **下个目标**：第 4 板块——文件读写（`open()` / `with` / `read()`/`write()` / `json` / `csv` / `pathlib`）。
