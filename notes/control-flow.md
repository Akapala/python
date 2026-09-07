# Python 控制流与脚本基础

> 日期：2026-09-07
> 涵盖：while 循环、break/continue/return 作用域、try/finally 边界、print 隐藏参数、`__name__` 入口约定

---

## 1. `while` 循环：什么时候用 `while True`

| 写法 | 判断时机 | 适合场景 |
|------|---------|---------|
| `while 条件:` | **进入前**先判断 | "数到 10 停"、"读到文件末尾停" |
| `while True:` + `break` | **做完才判断** | "用户输入 q 才停"、"撞墙才停" |

```python
# 写法 1：进入前能判断的
i = 0
while i < 5:
    print(i); i += 1

# 写法 2：必须先做才知道
while True:
    cmd = input("输入 q 退出：")
    if cmd == 'q':
        break
```

**两个易踩点**：

- `while True` 忘了写 `break` → 真死循环 → **Ctrl + C** 强制中断
- 高速循环体内没有 `input()` / `sleep()` → CPU 跑满、风扇狂转

---

## 2. 三个跳转关键字

### 一句话对比

| 关键字 | 归属 | 效果 | 写错位置的报错 |
|--------|------|------|----------------|
| `break` | 循环 | 结束整个循环 | `'break' outside loop` |
| `continue` | 循环 | 跳过本轮剩余 | `'continue' not properly in loop` |
| `return` | 函数 | 结束整个函数（顺带结束里面所有循环） | `'return' outside function` |

### 关键事实

- **`break` / `continue` 只认循环，跟 `if` 无关**。`if xxx: break` 能跑，只是因为这个 `if` 嵌在循环里。
- **`return` 是最强跳出**——能一次跳出多层循环，办法是**把多层嵌套抽成函数 + `return`**。
- 三个都遵守 `try...finally`：**走之前一定执行 `finally`**（关文件、释放锁放这里最稳）。

### 经典坑：`while` + `continue` 跳过递增

```python
i = 0
while i < 5:
    if i == 2:
        continue      # ☠️ 跳过下面 i += 1 → 死循环
    i += 1
```

`for` 循环没这问题（递增由迭代器自动完成）。

### 彩蛋：`for...else`

```python
for x in items:
    if x == target:
        break
else:                  # 循环跑完都没 break → 才走这里
    print("没找到")
```

---

## 3. `try / finally` 的边界

### 模块顶层可以写（但要小心）

`try / except / finally` 是**语句**，不属于任何函数或循环，模块顶层随便写：

```python
f = open("data.txt", encoding="utf-8")
try:
    print(f.read())
finally:
    f.close()
```

### `try` 不会"解锁"任何东西

**`try` 块里的 `break` / `continue` / `return` 该受什么限制还受什么限制**：

```python
try:
    break     # ✗ SyntaxError：没循环包着
finally:
    pass

try:
    return    # ✗ SyntaxError：不在函数里
finally:
    pass
```

### 两个 finally 坑

```python
def f():
    try:
        return 1 / 0        # 本应抛 ZeroDivisionError
    finally:
        return 999          # ☠️ 异常被悄悄吞掉，返回 999
```

所以 **`finally` 里只做收尾，别写 `return`**。

---

## 4. `print` 的隐藏参数

### 完整签名

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

| 参数 | 管什么 | 默认 |
|------|--------|------|
| `sep` | 多个值**之间**夹什么 | `' '`（空格） |
| `end` | 全部打完**末尾**接什么 | `'\n'`（换行） |
| `flush` | 是否立刻刷出 | `False`（有缓冲） |

### `print()` 等价于 `print("", end="\n")`

只换行、不输出内容，常用于段落/分块间隔。

### 拼图案靠 `end=""`

```python
for i in range(3):
    for j in range(3):
        print("*", end="")   # 同一行连着打
    print()                  # 内层结束手动换行
# ***
# ***
# ***
```

### `flush=True` 用在进度条

```python
print("加载中", end="", flush=True)
```

不强制刷新，输出可能"卡着"不显示。

---

## 5. 脚本入口约定：`if __name__ == '__main__':`

### 核心：Python 没有 `main` 函数

| 语言 | 入口 |
|------|------|
| C/C++ | OS 找 `int main()` 调用 |
| **Python** | **整个 .py 文件就是入口**，从上到下顺序执行 |

### `__name__` 是什么

Python 加载每个文件时**自动**给它一个变量：

| 怎么运行的 | `__name__` 值 |
|-----------|---------------|
| `python foo.py` 直跑 | `'__main__'` |
| 别的文件 `import foo` | `'foo'`（模块名） |

### 标准模板（推荐）

```python
def main():
    # 真正的主逻辑全在这里
    print('call foo()'); foo()
    print('call bar()'); bar()

if __name__ == '__main__':
    main()       # 只剩一行调用
```

比"代码直接写 if 块里"更好：
1. **有独立作用域**——变量不污染模块全局
2. **可以被 import 后显式调用**——`from mymod import main; main()`
3. **方便传参与返回**——能 `main(argv)`、能 `return 退出码`

### `pass` 是占位符

```python
def main():
    # Todo: Add your code here
    pass    # 函数体不能空，先用 pass 占位
```

### 升级版（生产脚本长这样）

```python
import sys

def main():
    args = sys.argv[1:]      # 用户传的参数
    # ... 主逻辑 ...
    return 0                  # 0 = 成功

if __name__ == '__main__':
    sys.exit(main())          # 把退出码交给 OS
```

### 拼写检查

```python
__name__      # ✓ 两边各两个下划线
_name_        # ✗ AttributeError
__Main__      # ✗ 大小写错，永远为假
```

---

## 6. 今日练习（建议存到 `repository/src/basics/`）

| 题目 | 关键技巧 |
|------|---------|
| 斐波那契前 20 项 | `a, b = b, a + b` 元组同时赋值 |
| 100 以内素数 | 朴素 / 试除到 √n / 埃氏筛 |

埃氏筛核心：每次用最小的"素数"当筛子，从 `p*p` 起划掉所有倍数；起点必须是 `p*p`，不是 `p`。

---

## 易踩坑速查表

| 坑 | 现象 |
|----|------|
| 循环外写 `break` / `continue` | SyntaxError |
| `while` 里 `continue` 跳过 `i += 1` | 死循环 |
| `finally` 里写 `return` | 吞掉异常 / 覆盖返回值 |
| `print("ture")` | NameError（`True` 首字母大写） |
| `__name__` 拼成 `_name_` | AttributeError |
| 埃氏筛 `range(p, n+1, p)` | 把素数也划掉，结果全错 |
