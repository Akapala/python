"""第 5 课：random 模块 —— 随机星空

每次运行画面都不一样，这就是随机数的乐趣。

新知识点：
    * import random：用标准库里的随机数模块
    * randint(a, b)：闭区间 [a, b] 内的随机整数（注意：C 的 rand()%n 不包含右端点）
    * choice(列表)：从列表里随机挑一个元素
    * random()：0~1 之间的随机小数，常配合 if 做「按概率发生」
    * if / else：条件判断，用缩进来划分代码块

运行：
    python src/turtle/05_random_stars.py
"""

import random
import turtle

STAR_COUNT = 80        # 一共撒多少颗星
STAR_PROBABILITY = 0.35  # 其中有多大比例画成五角星，其余画成圆点


def star(t, size, color):
    """画一个实心的五角星。五角星每个顶点转 144 度，转 5 次正好回到原点。"""
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


screen = turtle.Screen()
screen.title("05 随机星空")
screen.bgcolor("midnightblue")
screen.setup(800, 600)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.penup()               # 全程抬笔：每颗星是独立图形，不要连成一条线

for _ in range(STAR_COUNT):
    x = random.randint(-380, 380)
    y = random.randint(-260, 260)
    size = random.randint(6, 22)
    color = random.choice(["white", "lightyellow", "cyan", "plum"])

    t.goto(x, y)

    # random.random() < 0.35 的概率成立 → 约三分之一的星画成五角星
    if random.random() < STAR_PROBABILITY:
        star(t, size, color)
    else:
        # dot(直径, 颜色)：画一个实心圆点
        # 这里用 // 整除而不是 / —— 第 02 课讲过：/ 恒得小数，// 才得整数，
        # 而 dot 的直径参数要求是整数
        t.dot(size // 2, color)

screen.update()
turtle.done()
