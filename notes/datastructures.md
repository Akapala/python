# datastructures 板块 · 字符串和常用数据结构

> **来源**：`docs/07.字符串和常用数据结构.md`
> **代码目录**：`src/datastructures/`，编号 `01` ~ `07`
> **整理日期**：2026-09-08
> **受众**：有 C/C++ 基础、正在系统学 Python 的自己

---

## 1. 字符串：不可变 + 切片 + 格式化

字符串是**不可变**序列（改字符只能生成新串，不能原地改某个字符）。

| 操作 | 语法 | 说明 |
|------|------|------|
| 拼接 | `s1 + s2` | 生成新串 |
| 重复 | `s * 3` | 内容重复 3 遍 |
| 成员 | `'ll' in s` | 子串判断 |
| 下标 | `s[2]` / `s[-1]` | 支持**负下标**（倒数） |
| 切片 | `s[2:5]` / `s[::2]` / `s[::-1]` | 左闭右开；`[::-1]` = 反转 |

**转义与原始字符串**：`\n` 换行、`\t` 制表、`\'` / `\\` 表示字面符号；在串前加 `r` 让反斜杠不当转义：`r'\n'` 就是两个字符 `\` 和 `n`。

**三种格式化**（推荐 f-string）：

```python
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))        # 老式 % 占位符
print('{0} * {1} = {2}'.format(a, b, a * b)) # str.format
print(f'{a} * {b} = {a * b}')                # f-string（最简洁，3.6+）
```

**常用方法**：`len / find(找不到返回 -1) / startswith / endswith / strip / upper / capitalize / title`。

**C/C++ 对照**：字符串在 C 里是 `char[]`（可改），C++ 的 `std::string` 也允许改单个字符；Python 字符串**整体不可变**，这点更像 Java 的 `String`。

---

## 2. 列表：可变容器 + 增删 + 排序

列表是**有序、可变、可重复**的序列，最常用。

```python
list1 = [1, 3, 5, 7, 100]
list1[2] = 300                  # 改元素
list1.append(200)               # 尾部追加
list1.insert(1, 400)            # 位置 1 插入
list1 += [1000, 2000]           # 合并（等价于 extend）
list1.remove(3)                 # 按值删（不存在抛 ValueError）
list1.pop(0)                    # 按下标删，返回被删元素
list1.clear()                   # 清空
```

**三种遍历**：

```python
for index in range(len(list1)):      # 需要下标
    print(list1[index])
for elem in list1:                   # 只要值
    print(elem)
for index, elem in enumerate(list1): # 索引 + 值
    print(index, elem)
```

**切片复制 / 反转**：`fruits3 = fruits[:]`（复制一份新列表）；`fruits[::-1]`（反转拷贝）。

**排序**：`sorted(list)` 返回**新列表、不改原列表**；`list.sort()` **原地改、返回 `None`**。

---

## 3. 推导式与生成器：空间 vs 时间

```python
f = [x ** 2 for x in range(1, 1000)]   # 列表推导式：一次性算完，占内存
g = (x ** 2 for x in range(1, 1000))   # 生成器表达式：惰性，用到才算，几乎不占内存
```

- `[]` 创建时就把所有结果算好塞进内存；`()` 只记住"怎么算"，取数时才现算。
- `sys.getsizeof(f)` 比 `sys.getsizeof(g)` 大得多（**注意：用 `sys.getsizeof` 必须先 `import sys`**）。
- `yield` 把普通函数变成生成器函数：每次执行到 `yield` 就"暂停"交出一个值。

```python
def fib(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a
```

**C/C++ 对照**：生成器 ≈ 惰性迭代器（`std::generator` / 手写 iterator），避免一次性构造大容器。

---

## 4. 元组：不可变 + 为何需要

元组用 `()`，元素**不能改**（不可变对象）。想"改"只能让变量重新引用新元组。

```python
t = ('骆昊', 38, True, '四川成都')
for member in t:        # 循环变量名随意，不叫 member 也行
    print(member)
person = list(t)        # 元组 -> 列表（列表可改）
fruits_tuple = tuple(['apple', 'banana'])  # 列表 -> 元组
```

**为什么还要元组**（相对列表的优势）：
1. 不可变 → 更安全（不会有线程并发改坏状态）、更易维护；
2. 创建更快、占用内存更小；
3. 函数返回多个值，本质就是返回一个元组。

**C/C++ 对照**：类似 `const` 修饰的数组 / `std::tuple`，但 Python 里是"默认不可变"而非"默认可变 + 手动 const"。

---

## 5. 集合：去重 + 集合运算

集合 `{}` / `set()`，**元素不重复、无序**（不能按下标取）。

**增删**：

```python
set1.add(4)                 # 加单个
set2.update([11, 12])       # 批量加
set2.discard(5)             # 没有也不报错
set2.remove(4)              # 没有就 KeyError（删前先 `in` 判断更稳）
set3.pop()                  # 随机弹一个（无序）
```

**集合运算**（运算符 vs 方法，结果一致但运算符更直观）：

| 运算 | 运算符 | 方法 | 含义 |
|------|--------|------|------|
| 交集 | `&` | `intersection` | 两者都有 |
| 并集 | `|` | `union` | 合并去重 |
| 差集 | `-` | `difference` | 在左不在右（单向） |
| 对称差 | `^` | `symmetric_difference` | 只在一个里（双向，排除公共） |

子集/超集：`set2 <= set1`（子集）、`set1 >= set3`（超集）。

**关键区分**：
- `discard` 删不到**不报错**，`remove` 删不到**抛 `KeyError`**；
- **差集 `A - B` 是单向**（站在 A 立场减 B），**对称差 `A ^ B` 是双向**（两边独有合体，`A^B == B^A`）。

---

## 6. 字典：键值映射

字典 `{键: 值}`，键唯一、无序，每个元素是"键值对"。

```python
scores = {'骆昊': 95, '白元芳': 78}
items2 = dict(zip(['a', 'b', 'c'], '123'))     # zip 把两序列"拉链"成对
items3 = {num: num ** 2 for num in range(1, 10)} # 字典推导式

print(scores['骆昊'])            # 下标取值（键不存在 KeyError）
for key, value in scores.items(): # items() 同时拿键值
    print(key, value)

scores['白元芳'] = 65            # 有则改、无则增
scores.update(冷面=67, 方启鹤=85)
print(scores.get('武则天', 60))  # get 可设默认值，键不存在返回 60 而非报错

scores.pop('骆昊', 100)          # 删键返回值，给默认防 KeyError
scores.popitem()                 # 删"最后"插入的键值对
scores.clear()
```

**`d[key]` vs `d.get(key, 默认)`**：前者键缺失直接 `KeyError`；后者安全返回默认值，读可选键优先用 `get`。

---

## 7. 综合练习速记（代码见 `07_exercises.py`）

| 函数 | 思路 | 关键点 |
|------|------|--------|
| `generate_code` | 从字符表随机抽 `code_len` 个 | `random.randint` 下标；字符串 `+` 拼接 |
| `get_suffix` | `rfind('.')` 找最后的点 | 判断点合法位置；`has_dot` 控制是否带点 |
| `max2` | 先定前两大，再单次遍历比较 | 一次遍历，`m1`/`m2` 同时维护 |
| `which_day` | 闰年决定 2 月天数，`range(month-1)` 累加 | 用 `[平年表, 闰年表][is_leap_year(year)]` 二维选取 |

**核心思想**（与函数板块一致）：把独立功能抽成函数（如 `is_leap_year`），再用**组合**解决复杂问题。

> 文档里还有三个综合大案例——双色球选号（`random.sample`）、约瑟夫环（列表模拟环形）、井字棋（字典存棋盘）、以及杨辉三角（嵌套列表）、跑马灯（字符串切片滚动），学有余力自行拓展。

---

## 8. 调试收获 ★：可变对象方法常常返回 `None`

这是本板块最容易和"函数返回要兜底"那节课（functions 笔记第 8 节）混淆的坑。

**现象**：很多**原地修改**列表/字典/集合的方法，返回值是 `None`，而不是"改完后的对象"：

```python
list1 = [3, 1, 2]
result = list1.sort()          # result 是 None！list1 自己被改了
print(result)                  # None  ← 以为拿到了排好序的列表，其实没有

# 同样返回 None 的还有：
list1.append(4)   # None
list1.clear()     # None
scores.pop('x')   # 这个例外：返回被删的值
set1.add(1)       # None
```

**对比 `sorted`**：`sorted(list1)` 才返回**新列表**且不改原列表；想"既要新列表又保留原列表"用 `sorted`，想"就地改省内存"用 `list1.sort()`。

**坑**：`x = my_list.sort()` 后拿 `x` 当列表用 → `AttributeError` / 类型推断成 `None`。

**教训（记住这条）**：
> **原地修改的方法返回 `None`，要"拿到结果"就用返回新对象的函数（`sorted`/`reversed`）或不把调用结果赋值。**
> 这与 functions 笔记的"函数任何路径都要返回合理类型"是同一枚硬币的两面：前者是"它**故意**返回 `None`"，后者是"它**漏写**了 return 才返回 `None`"——两者都会在严格类型检查 / 后续使用里炸出来。

---

## 9. 易踩坑速查表

| 坑 | 现象 / 后果 |
|----|------------|
| 字符串改单个字符 `s[0]='x'` | `TypeError`：字符串不可变 |
| `list1.sort()` 后赋值给变量 | 拿到 `None`，不是排好序的列表 |
| `d[key]` 键不存在 | `KeyError`；读可选键改用 `d.get(key, 默认)` |
| 集合按下标 `set1[0]` | `TypeError`：集合无序，不能下标 |
| `discard` vs `remove` | 删不到的元素：`discard` 不报错、`remove` 抛 `KeyError` |
| 差集 `A - B` 不等于对称差 `A ^ B` | 前者单向（只在 A 不在 B），后者双向（各自独有合体） |
| 生成器表达式用 `sys.getsizeof` | 必须先 `import sys`，否则 `NameError` |
| 元组"改元素" `t[0]=...` | `TypeError`；只能重新引用新元组 |
| 函数返回多值 | 本质是返回**元组**，可用 `a, b = f()` 解包 |

---

## 今日练习

1. 自己独立写出 `get_suffix` 和 `max2`（先别看 `07_exercises.py`），再对比。
2. 用生成器表达式改写"求 1~10 的平方和"，体会 `()` 与 `[]` 的内存差异（`sys.getsizeof` 验证）。
3. 设计一个 `dict` 存学生成绩，用 `get` 安全查询一个不存在的学生，再用 `items()` 遍历打印。
4. （拓展）把文档里的「杨辉三角」或「双色球选号」自己实现一遍，练习嵌套列表 / `random.sample`。
