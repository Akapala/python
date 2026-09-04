"""第 7 课：递归 —— 科赫雪花

递归的规则只有一句：
    画一条科赫曲线 = 把线段三等分，中间那一段换成向外凸出的尖角，
    然后对新生成的 4 条小线段，重复同样的操作。

「重复同样的操作」就是递归。深度 depth 决定重复几层。

新知识点：
    * 递归的两个要件：终止条件 + 向终止条件收敛的调用
    * 递归里 turtle 的角度要「有借有还」：左转 60 之后要记得右转 120 再左转 60
    * 用 tracer(0) 撑住深层递归：depth=4 时要画 3 * 4^4 = 768 条线段

运行：
    python src/turtle/07_snowflake.py
"""

import turtle

DEPTH = 4       # 递归深度。改成 0/1/2/3 观察变化；改成 6 以上会明显变慢


def koch(t, length, depth):
    """画一条科赫曲线：长度为 length，递归深度为 depth。"""
    if depth == 0:              # 终止条件：深度用光了就老老实实画直线
        t.forward(length)
        return                  # return 提前结束本次调用，不再往下走

    third = length / 3

    # 把一条线段拆成 4 段，每段继续递归
    koch(t, third, depth - 1)   # 第 1 段：平的
    t.left(60)                  # 左转 60 度
    koch(t, third, depth - 1)   # 第 2 段：斜上去
    t.right(120)                # 右转 120 度（回正再反向）
    koch(t, third, depth - 1)   # 第 3 段：斜下来
    t.left(60)                  # 再左转 60 度，方向回到水平
    koch(t, third, depth - 1)   # 第 4 段：平的


def snowflake(t, length, depth):
    """三条科赫曲线首尾相接、各自转 120 度，就是一片雪花。"""
    for _ in range(3):
        koch(t, length, depth)
        t.right(120)


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()


screen = turtle.Screen()
screen.title("07 科赫雪花：递归")
screen.setup(700, 700)
screen.bgcolor("#0d1b2a")
screen.tracer(0)          # 线段数量爆炸式增长，必须关掉逐帧动画

t = turtle.Turtle()
t.speed(0)
t.pencolor("deepskyblue")

jump(t, -160, 100)
snowflake(t, 320, DEPTH)

screen.update()
turtle.done()
