"""第 4 课：函数 —— 把「一片花瓣」封装成可以复用的零件

先写一个只画单片花瓣的函数，再用循环把它转一圈拼成花。
有了函数，换花瓣数、换大小、换颜色都只是改一行参数的事。

新知识点：
    * def 定义函数，括号里是参数，参数可以带默认值
    * 关键字实参：flower(t, petals=6, ...) 不用记参数顺序
    * begin_fill() / end_fill()：把围出来的封闭区域填上颜色
    * 函数可以接收一支画笔当参数，一支笔画完再换一支

运行：
    python src/turtle/04_flower.py
"""

import turtle


def petal(t, size, color):
    """画一片花瓣：两段 60 度的圆弧背靠背拼成一个尖角。"""
    t.color(color)          # 同时设置画笔色和填充色
    t.begin_fill()          # 开始记录填充区域
    for _ in range(2):
        t.circle(size, 60)  # circle(半径, 角度)：只画一段弧，不是整圆
        t.left(120)
    t.end_fill()            # 到这里把走过的封闭路径填色


def flower(t, petals=8, size=60, color="hotpink"):
    """把 petals 片花瓣绕一圈拼成一朵花。"""
    for _ in range(petals):
        petal(t, size, color)
        t.left(360 / petals)   # 每片花瓣之间转一个等分角度


def jump(t, x, y):
    """把画笔挪到 (x, y)，路上不留痕迹。这个操作太常用，值得单独封成函数。"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()


screen = turtle.Screen()
screen.title("04 花朵：函数封装")
screen.setup(800, 500)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)

# 同一个函数，换参数就是完全不同的花
jump(t, -200, 0)
flower(t, petals=6, size=70, color="hotpink")

jump(t, 0, 0)
flower(t, petals=8, size=60, color="gold")

jump(t, 200, 0)
flower(t, petals=12, size=45, color="skyblue")

# 花瓣层层叠叠：同一位置画两遍，第二遍小一点、转半格
jump(t, 0, -180)
flower(t, petals=10, size=55, color="orange")
flower(t, petals=10, size=35, color="yellow")

screen.update()
turtle.done()
