# functions 板块 · 函数和模块的使用

> **来源**：`docs/06.函数和模块的使用.md`
> **代码目录**：`src/functions/`，编号 `01` ~ `06`
> **整理日期**：2026-09-08
> **受众**：有 C/C++ 基础、正在系统学 Python 的自己

---

## 1. 为什么需要函数：消除重复

算组合数 `C(M,N) = M! / (N! · (M-N)!)`，朴素写法把「求阶乘」写了三遍。
**Fowler 名言：代码有很多种坏味道，重复是最坏的一种。**

把求阶乘抽成 `fac()`，需要的地方调用即可——这就是函数最核心的价值：**消灭重复、表达意图**。

> 小提示：`math.factorial` 已存在，真实项目直接 `from math import factorial`，不必自己造轮子。

---

## 2. 定义函数 `def`

| 要素 | Python | C/C++ 对照 |
|------|--------|-----------|
| 参数类型 | `def f(a):` **不声明**，运行时才定 | `void f(int a)` 必须声明 |
| 返回类型 | 不写，可返回任意类型 | 必须写在函数名前 |
| 重载 | **不支持**，靠默认参数 + 关键字实参 | 同名不同参数可重载 |

```python
def fac(num):
    """文档字符串，help(fac) 能看到"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result          # 没有 return 时默认返回 None
```

---

## 3. 参数：默认值 + 关键字实参（替代重载）

```python
def roll_dice(n=2):       # 默认参数
    ...
def add(a=0, b=0, c=0):
    return a + b + c

add()                     # 全用默认
add(1, 2, 3)              # 按位置
add(c=50, a=100, b=200)   # 关键字实参：不按顺序，可读
```

**C/C++ 对照**：Python 用「默认参数 + 关键字实参 + `*args`」达到函数重载的效果，
因为同名 `def` 后者覆盖前者（变量指向函数对象），**没有按签名分派**这一步。

---

## 4. 可变参数 `*args`

参数个数由调用者决定时，用 `*` 把位置参数收进元组：

```python
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

add()                     # 0
add(1, 2, 3, 5, 7, 9)    # 任意个
# 进阶：直接 sum(args)
```

**C/C++ 对照**：相当于 `initializer_list` 或可变参数模板，但 Python 调用方不用包一层 `{...}`。

---

## 5. 模块管理 + `__main__` 守卫

- 一个 `.py` 文件 = 一个**模块**；不同模块可以有同名函数，靠 `import` 区分来源。
- Python **无函数重载**：同文件里后定义的同名函数覆盖先定义的。
- `from module1 import foo` / `import module1 as m1`（用 `m1.foo()` 区分）。
- 连续 `from a import foo; from b import foo` → **后者覆盖前者**。

**守卫**：模块里要执行的代码用 `if __name__ == '__main__':` 包起来，
这样「被 import 时不跑，自己直跑时才跑」（直接运行 `__name__` 才是 `'__main__'`）。

**推荐骨架**：

```python
def main():
    ...

if __name__ == '__main__':
    main()
```

---

## 6. 变量作用域 LEGB

找变量顺序：**L**ocal → **E**nclosing（嵌套）→ **G**lobal → **B**uilt-in。

| 关键字 | 作用 | 示例 |
|--------|------|------|
| （无） | 读外部变量不用声明；**赋值**则新建局部 | `print(a)` 可读全局 `a` |
| `global` | 函数内改**全局**变量 | `global a; a = 200` |
| `nonlocal` | 内层函数改**嵌套**作用域变量 | 闭包里改外层 `count` |

**坑**：函数内给外部变量**赋值却没写 `global`** → 新建局部变量，外面那个不变；之后再读会 `UnboundLocalError`。
**建议**：尽量减少全局变量（作用域太广、生命周期太长、增加耦合）。

---

## 7. 综合练习速记（代码见 `06_exercises.py`）

| 函数 | 思路 | 关键点 |
|------|------|--------|
| `gcd(x, y)` | 从 `min` 往下试，第一个同时整除 x、y 的 factor | 见第 8 节「兜底」 |
| `lcm(x, y)` | `x * y // gcd(x, y)` | 用 `//` 整除 |
| `is_palindrome(n)` | 反转各位数字比较 | `n % 10` 取末位、`n //= 10` 去末位 |
| `is_prime(n)` | 试除到 `√n` | `math.isqrt(n)` 比 `int(n**0.5)` 精确 |
| 回文素数 | `is_palindrome(n) and is_prime(n)` | **组合两个已有函数** |

**核心思想**：把重复/独立功能抽成函数，再用函数**组合**解决复杂问题。

---

## 8. 调试收获 ★：`gcd` 一定要有 `return` 兜底

这是本板块最重要的调试教训。

**现象**：`gcd` 的 `return` 只写在 `for` 循环里的 `if` 分支内：

```python
def gcd(x, y):
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    # ← 没有兜底 return
```

- 类型检查器（basedpyright）发现「循环可能不返回」，把 `gcd` 推断为 `int | None`；
- 于是 `lcm` 里的 `x * y // gcd(x, y)` 报「`int` 与 `int | None` 不支持 `//`」；
- `lcm` 的返回类型也被拖累成 `int | Unknown`。

**修法**：补一个兜底 `return`，并标返回类型，让所有路径都返回 `int`：

```python
def gcd(x: int, y: int) -> int:
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1   # 兜底：factor 递减到 1 必同时整除，理论走不到这里
```

**教训（记住这条）**：
> **考虑要全面——任何情况都要有合理类型的返回值。**
> 函数存在「隐式返回 `None`」的路径时，严格类型检查一定会揪出来。显式兜底 `return` + 标注 `-> 类型`，既是正确性保证，也是给读代码人的交代。

---

## 易踩坑速查表

| 坑 | 现象 / 后果 |
|----|------------|
| 同文件同名函数 | 后者覆盖前者，只有一个生效 |
| `from a import foo; from b import foo` | 后者覆盖前者 |
| 函数内改外部变量没写 `global` | `UnboundLocalError` / 改不到外面 |
| `gcd` 只循环内 `return` | `int \| None` 推断，下游 `//` 报错 |
| `is_prime` 用 `int(n ** 0.5)` | 浮点取整误差 + `**0.5` 被推断 `Any`；改用 `math.isqrt(n)` |

---

## 今日练习

1. 自己独立写出 `gcd` / `is_prime`（先别看答案），再对比 `06_exercises.py`。
2. 把 `add(*args)` 改成支持「字符串拼接 / 列表合并」——体会 Python 鸭子类型的灵活。
3. 写两个同名 `foo()` 在两个模块里，用 `import ... as` 分别调用，验证不冲突。
