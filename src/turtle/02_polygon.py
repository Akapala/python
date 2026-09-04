"""第 2 课：从三角形到圆 —— 循环嵌套与循环变量

把「画一个正 n 边形」的规律写成公式：每画一条边，就转 360 / n 度。
边数越大越接近圆，36 边形肉眼已经看不出棱角。

新知识点：
    * 循环里面再套一层循环
    * enumerate()：同时拿到元素的「下标」和「值」
    * f-string：f"{n} 边" 把变量直接嵌进字符串
    * setheading(0)：把画笔方向复位，避免上一个图形把方向带跑偏

运行：
    python src/turtle/02_polygon.py
"""

import turtle

# 模块级常量按 Python 约定用大写字母命名（提示自己：这个值不打算改）
SHAPES = [3, 4, 5, 6, 8, 12, 36]   # 依次画几边形
SIDE = 50                           # 每条边的长度

screen = turtle.Screen()
screen.title("02 从多边形到圆")
screen.setup(900, 500)

t = turtle.Turtle()
t.pensize(2)
t.speed(6)

# enumerate(SHAPES) 每次吐出一对 (下标, 值)，用两个变量接住
# 第一轮：i=0, n=3   第二轮：i=1, n=4   ……
for i, n in enumerate(SHAPES):
    x = -350 + i * 100        # 用下标算横坐标，把图形排成一排

    # 抬笔移动：penup 之后走的路不会留下痕迹，pendown 之后才开始画
    t.penup()
    t.goto(x, -40)
    t.setheading(0)           # 方向归零：朝正右方
    t.pendown()

    for _ in range(n):        # 内层循环：画 n 条边
        t.forward(SIDE)
        t.left(360 / n)       # 关键公式：外角和恒等于 360 度

    # 在图形下方标注边数
    t.penup()
    t.goto(x, -110)
    t.write(f"{n} 边", align="center", font=("Microsoft YaHei", 11, "normal"))

# 对比：turtle 其实内置了画圆的方法
t.penup()
t.goto(0, 160)
t.setheading(0)
t.pendown()
t.pencolor("tomato")
t.circle(45)                  # circle(半径)：本质是画一个边数很多的正多边形
t.penup()
t.goto(0, 95)
t.write("真正的圆：t.circle(45)", align="center", font=("Microsoft YaHei", 11, "normal"))

turtle.done()
