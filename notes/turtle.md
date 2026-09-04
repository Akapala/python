# turtle 板块 · 从画正方形到写贪吃蛇

> **适用对象**：有 C/C++ 基础，正在系统学 Python
> **环境**：Python 3.12 + tkinter（turtle 是标准库，**不需要** `pip install`）
> **代码目录**：`src/turtle/`，编号 `01` ~ `08`
> **配套规则**：代码里的逐行说明写在注释中；本篇负责讲清「为什么这么写」和「容易踩什么坑」

---

## 目录

| 编号 | 代码文件 | 画出什么 | 核心 Python 知识点 | 难度 |
|:---:|---|---|---|:---:|
| 00 | —— | 开课前必读 | 运行方式、坐标系、三个收尾动作 | ★ |
| 01 | `01_square.py` | 红色正方形 | `for` / `range()`、画笔对象 | ★ |
| 02 | `02_polygon.py` | 三角形→圆 | 循环嵌套、`enumerate`、f-string | ★★ |
| 03 | `03_color_spiral.py` | 彩色螺旋 | 列表、取余 `%`、`tracer/update` | ★★ |
| 04 | `04_flower.py` | 花朵图案 | `def` 函数、默认参数、填充 | ★★ |
| 05 | `05_random_stars.py` | 随机星空 | `random` 模块、`if/else` | ★★ |
| 06 | `06_click_board.py` | 鼠标画板 | 事件回调、闭包、`global` | ★★★ |
| 07 | `07_snowflake.py` | 科赫雪花 | 递归、分形 | ★★★ |
| 08 | `08_snake_game.py` | 贪吃蛇 | 综合项目：列表当队列、`ontimer` | ★★★★ |

学习建议：**按编号顺序来**，每课都动手改一改参数再运行。看代码只能得到 30%，改代码才能得到 100%。

---

## 00 · 开课前必读

### 0.1 怎么运行

在仓库根目录下打开终端：

```bash
python src/turtle/01_square.py
```

会弹出一个窗口，画完停在那里。关闭窗口，程序结束。

### 0.2 坐标系和方向（和数学课一致，和屏幕坐标相反）

```
              +y（上）
                │
                │   画笔默认朝向 ──▶ +x（右）
      原点 (0,0) ┼────────────────
                │
                │
```

- 原点在**画布正中央**，不是左上角（这里和绝大多数图形库不一样）
- `x` 向右为正，`y` **向上**为正（屏幕坐标系是向下为正，别搞混）
- 画笔出生时朝向**正右方**（东）
- `left()` 逆时针转，`right()` 顺时针转，单位是**度**不是弧度
- `goto(x, y)` 是**绝对**移动；`forward()` 是**相对**移动（沿当前朝向）

### 0.3 三个必须记住的收尾动作

| 动作 | 作用 | 忘了会怎样 |
|---|---|---|
| `turtle.done()` | 启动事件循环，让窗口停住 | 画完立刻闪退，什么都看不见 |
| `screen.tracer(0)` | 关掉逐帧动画，先画在后台 | 图形多的时候慢到你想砸键盘 |
| `screen.update()` | 配合 `tracer(0)`，一次性显示 | 窗口一片空白，以为程序坏了 |

**配对口诀**：写了 `tracer(0)`，最后一定要有 `update()`。

### 0.4 三个一定会踩的坑（先记住，能省两小时）

**坑 1：文件名绝对不能叫 `turtle.py`**

```text
src/turtle/turtle.py   ← 灾难
```

Python 找模块时先找当前目录，你的文件会把标准库的 `turtle` 顶掉，
`import turtle` 会 import 到你自己那个文件，然后报各种莫名其妙的错。
文件夹叫 `turtle` 是安全的（我们就是这么做的），文件不行。

**坑 2：注册回调时多写了括号**

```python
t.ondrag(draw)      # 对：把函数交出去，等事件发生时再调用
t.ondrag(draw())    # 错：现在就调用一次，然后把返回值 None 注册进去
```

**坑 3：改了 `tracer(0)` 却要做交互**

第 06 课的画板**不能**用 `tracer(0)`。交互程序必须实时刷新，
你关掉动画又忘了 `update()`，画的时候就什么都不显示。

### 0.5 调试小技巧

程序报错时，**从最后一行往上读**。Python 的报错信息最后一行是错误类型，
倒数第二行开始往上是调用栈，最上面那行才是真正出错的位置。

```text
Traceback (most recent call last):
  File "src/turtle/01_square.py", line 25, in <module>   ← 先看这里
    t.forward(100)
NameError: name 't' is not defined                        ← 再看这里：t 没定义
```

---

## 01 · 正方形：`for` 循环

> 代码：`src/turtle/01_square.py`

### 这节课做了什么

把仓库里已有的 `src/hello_world.py`（重复 4 遍的 `forward` + `right`）
改写成 3 行循环。那份原始代码保留在原地，方便你对比。

### 关键代码

```python
t = turtle.Turtle()      # 创建画笔对象
t.pensize(4)
t.pencolor("red")
t.speed(3)

for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

### 知识点

**1）两种写法：模块函数 vs 画笔对象**

| 写法 | 示例 | 特点 |
|---|---|---|
| 模块级函数 | `turtle.forward(100)` | 只有一支默认画笔，写起来短 |
| 画笔对象 | `t = turtle.Turtle()`<br>`t.forward(100)` | 可以创建多支笔，各有各的颜色粗细 |

`src/hello_world.py` 用的是第一种。从这节课开始我们统一用第二种：
画多支笔、做交互，都必须要对象。**现在改习惯，后面不用返工。**

**2）`for _ in range(4)`**

`range(4)` 产生 `0, 1, 2, 3` 四个数，所以循环体执行 4 次。
循环变量这一轮用不上，按 Python 约定写成下划线 `_`，
这是在告诉读代码的人「这个变量我故意不用」。

**3）`turtle.done()` 和 `mainloop()`**

完全等价，都是启动事件循环保持窗口。`done()` 更常用。

### C++ 对照

```cpp
for (int i = 0; i < 4; i++) {   // C++：自己管理计数器和步长
    forward(100);
    right(90);
}
```

```python
for _ in range(4):              # Python：range 负责产生数列
    t.forward(100)
    t.right(90)
```

差别不在长短，在**思维方式**：C++ 你写的是「计数器怎么变」，
Python 你写的是「要几个」。遍历列表、字符串、文件时这个差别会更明显。

### 常见坑

- 忘了 `turtle.done()` → 窗口一闪而过
- 缩进写错 → Python 用缩进划分代码块，没有 `{}`，也没有 `end`
- 循环体里漏写 `t.right(90)` → 画出来是一条直线（转都不转，可不就是直线）

### 练习

1. 把正方形改成**长方形**（长 150 宽 80），提示：循环写 4 次行不通了，想想要怎么写
2. 画一个**等边三角形**（每步转 120 度）
3. 画**三个叠在一起的正方形**，每个比上一个大 40 像素

---

## 02 · 从多边形到圆：循环嵌套

> 代码：`src/turtle/02_polygon.py`

### 这节课做了什么

把「画正 n 边形」总结成一个公式，然后一口气画出 3、4、5、6、8、12、36 边形，
看它们怎么一步步逼近圆。

### 关键代码

```python
for i, n in enumerate(SHAPES):        # 外层：每种图形画一遍
    x = -350 + i * 100                # 用下标算横坐标
    t.penup()
    t.goto(x, -40)
    t.setheading(0)                   # 方向复位
    t.pendown()

    for _ in range(n):                # 内层：画 n 条边
        t.forward(SIDE)
        t.left(360 / n)               # 核心公式

    t.penup()
    t.goto(x, -110)
    t.write(f"{n} 边", align="center", font=("Microsoft YaHei", 11, "normal"))
```

### 知识点

**1）核心公式：`360 / n`**

画完一条边，画笔转过的角度叫**外角**。绕图形走一圈回到原点、方向也复原，
转过的角度总和必然是 360 度。所以正 n 边形每次转 `360 / n`。

- 三角形：转 120 度
- 正方形：转 90 度
- 36 边形：转 10 度 → 已经是圆的形状了

**2）`enumerate()`：同时拿到下标和值**

```python
for i, n in enumerate([3, 4, 5]):
    # i = 0, 1, 2        ← 下标，用来算位置
    # n = 3, 4, 5        ← 值，用来算角度
```

这是 Python 里非常高频的写法，替代 C++ 里 `for (int i = 0; i < v.size(); i++) v[i]` 的套路。

**3）`setheading(0)`：方向复位**

每个图形画完，画笔朝向已经被转走了。不复位的话，下一个图形会歪着长出去。
**这是 turtle 最常见的 bug 之一。**

**4）f-string**

```python
f"{n} 边"                    # 把变量 n 的值插进字符串
f"得分：{score} 最高：{best}"  # 可以插多个，还能写表达式 f"{a + b}"
```

字符串前面加 `f`，花括号里写变量名。比 C++ 的 `std::to_string` 拼接或 `printf` 的 `%d` 好用太多。

**5）`penup()` / `pendown()`**

抬笔移动不留痕迹。turtle 的笔默认是「落着」的，
所以只要你想「瞬移」到别处，**抬笔 → goto → 落笔**这三步必须成套出现。

### 常见坑

- 忘了 `setheading(0)` → 图形歪七扭八，越画越偏
- 用了 `t.goto()` 但没 `penup()` → 图形之间连出一条斜线
- `360 / n` 在 Python 3 里永远得到小数（`/` 是真除法），
  想要整除得写 `//`。这里我们要的就是小数，别手贱改。

### 练习

1. 让边数从 3 一直循环到 20，看图形怎么变成圆
2. 改成画**五角星**（每次转 144 度，画 5 笔）
3. 给每个图形换一种颜色（提示：准备一个颜色列表，用 `i % len(颜色列表)` 取）

---

## 03 · 彩色螺旋：列表与取余

> 代码：`src/turtle/03_color_spiral.py`

### 这节课做了什么

步长随循环变量一点点变长、颜色按顺序轮换，300 步之后得到一朵彩色星芒螺旋。

### 关键代码

```python
screen.tracer(0)          # 关掉逐帧动画

COLORS = ["#ff4d4d", "#ffb84d", "#ffe14d", "#4dff88", "#4dd2ff", "#b84dff"]
t = turtle.Turtle()
t.speed(0)

for i in range(300):
    t.pencolor(COLORS[i % len(COLORS)])   # 取余 → 下标绕圈
    t.forward(i * 0.6 + 3)
    t.right(59)                            # 59 度：刻意不能整除 360

screen.update()           # 一次性显示
```

### 知识点

**1）列表 `list`**

```python
COLORS = ["#ff4d4d", "#ffb84d", "#ffe14d"]
COLORS[0]        # "#ff4d4d"，下标从 0 开始
len(COLORS)      # 3，元素个数
COLORS[-1]       # "#ffe14d"，负数下标从末尾数，这是 Python 的便利之处
```

C++ 对照：`vector<string>`。区别是 Python 的 list 可以混装任意类型：
`[1, "hello", 3.14, True]` 完全合法。

**2）取余 `%` 让下标绕圈**

```
i        :  0  1  2  3  4  5  6  7  8 ...
i % 6    :  0  1  2  3  4  5  0  1  2 ...
```

`i % len(COLORS)` 的结果永远落在 `0 ~ len-1` 之间，**永远不会越界**。
这是「循环使用一个列表」的标准做法，做游戏动画、轮播图全都靠它。

**3）为什么是 59 度**

转 90 度 → 4 次回到原点，画出来是方框螺旋。
转 60 度 → 6 次回到原点，是六角螺旋。
转 **59 度** → 永远回不到原点，线条才会不断错位、长出星芒。

**动手试试**：`59` 改成 `60`、`89`、`121`、`170`，每一个都是完全不同的图案。

**4）`tracer(0)` + `update()` 提速**

默认 turtle 会把每一小段线都画给你看，300 段就要等 300 次。
`tracer(0)` 说「先别显示」，`update()` 说「好了，一次性显示」。

对比实验：把 `tracer(0)` 那行注释掉再运行，你会立刻感受到区别。

### 常见坑

- 写了 `tracer(0)` 忘了 `update()` → 窗口全黑/全白，什么都没有
- 颜色名写错（比如 `"bleu"`）→ turtle 会抛 `TurtleGraphicsError`。
  不确定就用十六进制 `#RRGGBB`，我们这里用的就是它
- `speed(0)` 和 `tracer(0)` 是两回事：前者管画笔移动速度，后者管画面刷新

### 练习

1. 把 `range(300)` 改成 `range(600)`，看图案怎么变密
2. 反过来画：让步长从大到小（`300 - i * 0.5`），得到向内收的螺旋
3. 画**双层螺旋**：先画一个顺时针的，抬笔回中心，再画一个逆时针的

---

## 04 · 花朵：函数封装

> 代码：`src/turtle/04_flower.py`

### 这节课做了什么

先写一个只画「单片花瓣」的函数，再用循环把它转一圈拼成花。
同一个函数换参数，就能变出完全不同的花。

### 关键代码

```python
def petal(t, size, color):
    """画一片花瓣：两段 60 度的圆弧背靠背拼成尖角。"""
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(size, 60)     # circle(半径, 角度)：只画一段弧
        t.left(120)
    t.end_fill()


def flower(t, petals=8, size=60, color="hotpink"):
    """把 petals 片花瓣绕一圈拼成一朵花。"""
    for _ in range(petals):
        petal(t, size, color)
        t.left(360 / petals)
```

### 知识点

**1）`def` 定义函数**

```python
def 函数名(参数1, 参数2=默认值):
    """文档字符串，用 help(函数名) 能看到"""
    函数体
    return 返回值      # 没有 return 时默认返回 None
```

和 C++ 最大的三个区别：

| | C++ | Python |
|---|---|---|
| 参数类型 | `void f(int a)` 必须声明 | `def f(a)` 不声明，运行时才确定 |
| 返回值类型 | 必须写在函数名前 | 不写，可以返回任意类型 |
| 重载 | 同名不同参数可以重载 | 不能重载，靠默认参数 + 关键字实参解决 |

**2）关键字实参**

```python
flower(t, petals=6, size=70, color="hotpink")
```

带上参数名调用，**不用记顺序**，可读性还好。
前 4 课你写过的 `font=("Microsoft YaHei", 11, "normal")` 就是这么回事。

**3）`circle(半径, 角度)` 画弧**

第二个参数给了角度就只画一段弧，不给就是画整圆。这是花瓣、波浪线的万能工具。

**4）填充三件套**

```python
t.begin_fill()   # 开始记录路径
# ... 画一个封闭图形 ...
t.end_fill()     # 把围出来的区域填上当前颜色
```

`t.color(c)` 一次性设置笔色和填充色；想分开就用 `pencolor()` + `fillcolor()`。

**5）把画笔当参数传**

```python
def petal(t, size, color):   # t 是参数，不是全局变量
```

这样同一套函数可以服务多支不同的笔。等你要画多支笔的动画时，会感谢这个决定。

### 常见坑

- 函数定义必须在使用**之前**（模块层代码是从上往下执行的）
- `begin_fill()` 没有配对 `end_fill()` → 图形显示不完整
- 路径没封闭就用 `end_fill()` → 填充区域形状奇怪（turtle 会自动连首尾）
- 忘写 `t.end_fill()` 之前的 `t.left()` → 花瓣叠在一起看不出层叠

### 练习

1. 画一朵 **20 片花瓣**的花，观察它变成了什么形状
2. 给花朵加**花茎和叶子**（提示：画一条向下的绿色粗线 + 两片小花瓣）
3. 画一束花：用 `jump()` 把 5 朵不同颜色的花摆在一条弧线上

---

## 05 · 随机星空：`random` 模块

> 代码：`src/turtle/05_random_stars.py`

### 这节课做了什么

在深蓝背景上随机撒 80 颗星，其中约 1/3（按概率）画成实心五角星，其余画成圆点。
每一颗的位置、大小、颜色都是随机的，所以**每次运行画面都不一样**——这就是随机数的乐趣。

### 关键代码

```python
import random

STAR_COUNT = 80            # 一共撒多少颗星
STAR_PROBABILITY = 0.35    # 约 35% 画成五角星，其余画圆点

def star(t, size, color):
    """实心五角星：每个顶点转 144 度，转 5 次正好回到原点。"""
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

for _ in range(STAR_COUNT):
    x = random.randint(-380, 380)        # 闭区间 [a, b]
    y = random.randint(-260, 260)
    size = random.randint(6, 22)
    color = random.choice(["white", "lightyellow", "cyan", "plum"])

    if random.random() < STAR_PROBABILITY:
        star(t, size, color)
    else:
        t.dot(size // 2, color)          # 实心圆点；直径要整数，所以 // 整除
```

### 知识点

**1）`import random`：标准库的随机数模块**

`random` 是 Python 自带的标准库，**不需要 `pip install`**。常用函数：

| 函数 | 作用 | 例子 |
|---|---|---|
| `randint(a, b)` | `[a, b]` 闭区间内的随机整数 | `randint(1, 6)` 等同掷骰子 |
| `choice(列表)` | 从列表里随机挑一个元素 | `choice(["红", "绿", "蓝"])` |
| `random()` | `[0, 1)` 之间的随机小数 | 配 `if` 做「按概率发生」 |
| `randrange(起, 止, 步长)` | 按步长取随机数 | 第 08 课用它对齐网格 |

**2）`if / else`：用缩进划分代码块**

```python
if random.random() < 0.35:
    star(t, size, color)    # 概率成立走这里
else:
    t.dot(size // 2, color) # 否则走这里
```

和 C++ 对比：Python **没有 `{}`、没有 `then/endif`**，靠**缩进**判断谁属于哪个分支。
缩进错了逻辑就错了，而且编辑器不会像 C++ 缺大括号那样报错——这是新手最常栽的地方。

**3）`randint(a, b)` 是闭区间**

注意右端点 **包含** b。对比 C 的 `rand() % n` 得到 `[0, n-1]`，两者习惯不同，移植时要当心。

**4）`dot(直径, 颜色)`：实心圆点**

直径参数要求是整数，所以这里用 `//` 整除（第 02 课讲过：`/` 恒得小数，`//` 才得整数）。

### C++ 对照

```cpp
#include <cstdlib>
srand(time(nullptr));
int x = rand() % 761 - 380;   // [0,760] 再平移 → [-380, 380]
                             // 注意：rand()%n 是 [0, n-1]，右端不含 n
```
```python
x = random.randint(-380, 380)   # 直接给区间，右端包含
```

差别不在长短，在**心智负担**：C 要先 `%` 取模再平移、还要记得 `srand` 播种；Python 一行到位。

### 常见坑

- 写了 `t.dot()` 但直径是小数（`size / 2`）→ 报错，记得 `//`
- 忘记设背景色，星点在白底上几乎看不见
- `if` 分支里的语句缩进没对齐 → 逻辑悄悄错位

### 练习

1. 把 `STAR_PROBABILITY` 改成 `0.6`，看五角星是不是明显变多
2. 加一颗「月亮」：在固定位置画一个大黄圆，再盖一个背景色的圆做缺口
3. 让星星大小整体变大（`size = random.randint(10, 40)`），观察效果

---

## 06 · 鼠标画板：事件回调

> 代码：`src/turtle/06_click_board.py`

### 这节课做了什么

前面 5 课都是「写好剧本，从头演到尾」。这一课反过来：**程序等着你操作**，
你拖鼠标、按键，它才响应。这叫**事件驱动**。

操作：左键拖拽画线；`1~5` 换色；`u` 抬笔/落笔切换；`+/-` 加粗减细；`c` 清屏。

### 关键代码

```python
is_first_drag = True       # 模块层共享状态

def draw(x, y):
    """鼠标拖拽时反复触发。"""
    global is_first_drag
    if is_first_drag:
        t.penup(); t.goto(x, y); t.pendown()
        is_first_drag = False
    else:
        t.goto(x, y)

def make_color_setter(color):
    """外层记住 color，返回内层函数——这就是闭包。"""
    def setter():
        t.pencolor(color)
    return setter

screen.listen()                       # 开键盘监听，少了它 onkey 全失效
t.ondrag(draw)                       # 传函数名字，绝不加括号
for key, color in COLORS.items():
    screen.onkey(make_color_setter(color), key)
```

### 知识点

**1）回调函数：把「函数本身」当参数传**

`ondrag(draw)` 不是调用 `draw`，而是把 `draw` 这个**函数对象**交出去。
等鼠标拖拽事件发生时，turtle 才替你去调用它。所以传的是**名字，不能加 `()`**。

**2）`global`：函数内修改模块层变量**

```python
def draw(x, y):
    global is_first_drag   # 声明：我要改的是外面的那个变量
    is_first_drag = False
```

如果函数里**给**某个变量赋值，而它又定义在函数外面，就必须先写 `global` 声明。
否则 Python 会认为你在创建**局部**变量，外面那个完全没动，还会在读取时报 `UnboundLocalError`。

**3）闭包 / 工厂函数：绕开「回调不能传参」的限制**

`onkey(函数, 按键)` 要求被注册的函数**不能有参数**，可 `set_color("red")` 明明需要颜色。
办法是写一个外层函数 `make_color_setter(color)`，它记住 `color`，返回一个不带参数的内层 `setter`：

```python
def make_color_setter(color):
    def setter():
        t.pencolor(color)   # 内层用到了外层的 color —— 这就是闭包
    return setter
```

**4）`screen.listen()`：开启键盘监听**

漏了这句，`onkey` 全部失效，按键毫无反应。这是交互程序的标配。

**5）`isdown()` / `clear()`**

- `t.isdown()`：查询当前笔是否落着（用于切换抬落笔）
- `t.clear()`：只擦掉这支笔画过的痕迹，背景色不动（比 `screen.clear()` 温柔）

### 常见坑

- 注册时多写括号：`t.ondrag(draw())` → 当场调用一次，把 `None` 注册进去（前几课「坑 2」）
- 漏 `screen.listen()` → 键盘完全没反应
- 忘写 `global is_first_drag` → 切换抬笔后第一次拖拽又从中心拉直线

### 练习

1. 加一个「橡皮」键 `e`：把笔色设成背景色（白），实现擦除效果
2. 双击清屏：用 `screen.onkey(clear_all, "c")` 已有了，试试改成两根手指的连招
3. 加一个「保存」键 `s`：用 `screen.getcanvas().postscript(file="board.eps")` 把画布存成文件

---

## 07 · 科赫雪花：递归

> 代码：`src/turtle/07_snowflake.py`

### 这节课做了什么

用**递归**画分形雪花。规则只有一句：把线段三等分，中间换成向外凸的尖角，
然后对新生成的 4 条小线段重复同样的操作。`DEPTH` 决定重复几层。

### 关键代码

```python
def koch(t, length, depth):
    if depth == 0:                  # 终止条件：深度用光，老老实实画直线
        t.forward(length)
        return                      # 提前结束本次调用
    third = length / 3
    koch(t, third, depth - 1)       # 第 1 段：平
    t.left(60)
    koch(t, third, depth - 1)       # 第 2 段：斜上
    t.right(120)                     # 回正再反向
    koch(t, third, depth - 1)       # 第 3 段：斜下
    t.left(60)                       # 方向回到水平
    koch(t, third, depth - 1)       # 第 4 段：平

def snowflake(t, length, depth):
    for _ in range(3):
        koch(t, length, depth)
        t.right(120)
```

### 知识点

**1）递归的两个要件**

| 要件 | 这里怎么体现 |
|---|---|
| 终止条件 | `if depth == 0: 画直线 return` |
| 向终止收敛 | 每次调用 `depth - 1`，最终必然到 0 |

缺了终止条件就会无限递归、栈溢出崩溃；缺了收敛（比如忘了 `-1`）同样停不下来。

**2）角度要「有借有还」**

递归里画笔转向后要**复原方向**，否则下一层画出来的线会整体歪掉：

```
left(60)  →  right(120)  →  left(60)   # 净转 0 度，方向回到水平
```

这就是前面课反复提的 `setheading` 复位思想的递归版。

**3）`tracer(0)` 撑住深层递归**

`DEPTH=4` 时要画 `3 × 4⁴ = 768` 条线段，`DEPTH=6` 是 `3 × 4⁶ ≈ 12000` 条。
不开 `tracer(0)` 会慢到卡死。代码里 `screen.tracer(0)` + 末尾 `screen.update()` 一次性显示。

**4）`jump()`：起笔定位 + 方向复位**

和 02 课的 `setheading(0)` 同一思路——画多个图形前先把画笔「瞬移 + 归正」。

### 常见坑

- 忘记角度复原 → 雪花越画越歪，根本合不拢
- `DEPTH` 设到 7 以上 → 线段几万条，卡顿甚至无响应（自己算一下 `3×4^DEPTH`）
- 起笔没 `jump` 复位 → 雪花从画布中心斜着长出来

### 练习

1. 把 `DEPTH` 改成 `0,1,2,3` 各跑一次，观察「直线 → 锯齿 → 雪花」的演化
2. 画「科赫岛」：把 `snowflake` 的三条边改成画在正方形三条边上
3. 换个分形：写个 `tree(t, length, depth)`，每次分出左右两枝（经典递归树）

---

## 08 · 贪吃蛇：综合项目

> 代码：`src/turtle/08_snake_game.py`

### 这节课做了什么

把前面 7 课的家伙事儿全用上：列表、函数、循环、条件、事件、计时器。
方向键 / WASD 控制，吃到红方块加分，撞墙或撞到自己重来。

### 关键代码

```python
head = turtle.Turtle("square")
head.goto(0, 0)
head.direction = "stop"          # 给对象临时挂一个属性，记录方向

segments = []                    # 蛇身：每吃一个食物 append 一节

def follow():
    """身体跟随：从尾巴往头逐个接位。必须『从尾到头』。"""
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

def game_loop():
    """一帧的逻辑，末尾用 ontimer 再约一次自己 → 游戏主循环。"""
    follow(); move_head()
    # ... 撞墙 / 撞自己 / 吃食物 判定 ...
    screen.update()
    screen.ontimer(game_loop, DELAY)   # 约下一帧
```

### 知识点

**1）列表当队列 / 容器：`segments`**

蛇身是一串 `Turtle` 对象，**全装在一个列表里**：

```python
segments.append(new)   # 吃到食物，加一节
segments.clear()       # 重来时清空（注意不是 segments = []）
```

这再次体现了 Python 列表的特性：**能装任意对象**（这里是对象引用）。
清空时要用 `segments.clear()`（就地清空，所有引用同步），
而**不要写 `segments = []`**——后者只是把变量重新绑到新空列表，老列表里的旧节还挂在别处，重置会失效。

**2）从尾到头遍历：`range(len-1, 0, -1)`**

`follow()` 让每节挪到前一节的位置。顺序**必须**从尾巴开始：
若从头开始挪，前一节的位置刚被覆盖，后面几节就全叠在一起了。

**3）`screen.ontimer(函数, 毫秒)`：游戏主循环**

`turtle` 没有「每帧」概念，用 `ontimer` 注册一个定时回调，
再让 `game_loop` 在末尾**自己约自己**，就形成了持续的游戏循环。
`DELAY` 越小越快。`turtle.done()` 负责进入事件循环、让 `ontimer` 持续生效。

**4）动态属性：`head.direction = "stop"`（重点）**

Python 允许**随时给对象挂新属性**，不用在类里预先声明：

```python
head.direction = "stop"    # Turtle 类里本没有 direction，运行时照样能加
```

- 运行时完全合法，所以游戏能正常跑。
- 但**类型检查器（Pylance）不认**这种写法，会认为 `Turtle` 没有 `direction` 成员，
  于是每一处 `head.direction` 都画红线。你之前看到 08 课「全是报错」正是这个原因，
  已通过根目录的 `pyrightconfig.json` 把类型检查关掉解决（不影响运行）。
- 作为对照：若想让类型检查彻底安静，可改成独立全局变量 `direction = "stop"`，
  但那样就丢掉「动态加属性」这个教学点。

**5）网格坐标 + `distance` 碰撞**

所有位置都对齐到 `CELL` 的整数倍（食物用 `randrange(..., CELL)` 生成），
碰撞判断就简化为「两点距离是否小于半格」：`head.distance(food) < CELL / 2`。

**6）禁止 180 度掉头**

```python
def go_up():
    if head.direction != "down":   # 向上的同时若当前向下，忽略，防止直接撞脖子
        head.direction = "up"
```

### 常见坑

- `reset()` 里写 `segments = []` 而非 `.clear()` → 旧节没真正消失
- `game_loop` 末尾漏了 `screen.ontimer(game_loop, DELAY)` → 游戏只跑一帧就停
- `distance` 阈值写错（比如 `> CELL`）→ 明明没撞却判定撞了
- 把方向存在对象属性里却开着类型检查 → 满屏红线（见知识点 4）

### 练习

1. 把 `DELAY` 改成 `70`，体验加速；改成 `200` 体验减速
2. 加「穿墙」：撞墙不 `reset`，而是从对面出现（提示：坐标对 `2*BOUND` 取余）
3. 加音效 / 最高分持久化（把 `best` 写进文件，下次启动读取）

---

> **系列完。** 从画正方形到写贪吃蛇，你已经把 `for` / 列表 / 函数 / 事件 / 递归 / 定时器
> 这一整套 Python 基础走通了。下一步建议挑一个自己想做的 50 行小项目练手。
