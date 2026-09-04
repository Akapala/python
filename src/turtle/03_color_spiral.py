"""第 3 课：彩色螺旋 —— 列表、取余与绘图提速

让步长随循环变量一点点变长、颜色按顺序轮换，就得到一朵螺旋。

新知识点：
    * 列表 list：colors[0] 取第一个元素，len(colors) 取长度
    * 取余 %：让下标在 0~长度-1 之间循环，永远不会越界
    * screen.tracer(0) + screen.update()：关掉逐帧动画，画完一次性刷新
    * speed(0)：画笔本身也设为最快

运行：
    python src/turtle/03_color_spiral.py
"""

import turtle

# 十六进制颜色：#RRGGBB，每两位分别是红、绿、蓝的分量
COLORS = ["#ff4d4d", "#ffb84d", "#ffe14d", "#4dff88", "#4dd2ff", "#b84dff"]

screen = turtle.Screen()
screen.title("03 彩色螺旋")
screen.bgcolor("black")
screen.setup(800, 800)
screen.tracer(0)          # 关键：先别一帧一帧地画，全部画完再统一显示

t = turtle.Turtle()
t.width(2)
t.speed(0)                # 0 = 不动画，直接到位

for i in range(300):
    # i % len(COLORS) 的结果永远是 0、1、2、3、4、5 循环
    # 这是「让下标绕圈」最常用的一招
    t.pencolor(COLORS[i % len(COLORS)])

    t.forward(i * 0.6 + 3)   # 步长随 i 增长 → 越画越外扩
    t.right(59)              # 59 度刻意选一个不能整除 360 的数，才会出现星芒
                             # 试试改成 60、90、121，图案会完全不同

screen.update()           # 配合 tracer(0)：把刚才攒下的画面一次性显示出来
turtle.done()
