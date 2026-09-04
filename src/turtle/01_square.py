"""第 1 课：用循环画正方形

这节课改造仓库里已有的 src/hello_world.py，把重复 4 遍的命令交给 for 循环。

新知识点：
    * turtle.Turtle()   —— 创建一支属于自己的画笔（对象式写法）
    * for _ in range(4) —— 把一段代码重复执行 4 次
    * 循环嵌套          —— 外层控制画几个，内层控制一个图形画几条边
    * 变量累加          —— distance += 40，让每个正方形比上一个大 40 像素
    * turtle.done()     —— 让窗口停住，别画完就闪退

运行：
    python src/turtle/01_square.py
"""

import turtle

# Screen 是画布，Turtle 是画笔。后面所有课都会用这两个对象。
screen = turtle.Screen()
screen.title("01 正方形：for 循环")

t = turtle.Turtle()   # 变量名 t 只是习惯，你可以叫 pen、画笔、a 都行
t.pensize(4)          # 笔粗 4 像素
t.pencolor("red")     # 笔的颜色
t.speed(3)            # 1 最慢 ~ 10 最快，0 表示瞬间完成
distance = 50
# 正方形 = 「前进 100 步 + 右转 90 度」重复 4 次
# range(4) 会产生 0,1,2,3 四个数，循环体因此执行 4 次
# 循环变量这节课用不上，按约定写成下划线 _
for _ in range(3):
    t.penup()
    t.goto(-distance/2,distance/2)
    t.pendown()
    for _ in range(4):
        t.forward(distance)    # forward 简写是 fd
        t.right(90)     # right 简写是 rt，单位是「度」不是弧度
    distance=distance+40    

# 换算成改造前的样子，就是下面这样——看出循环的价值了吗？
# t.forward(100); t.right(90)
# t.forward(100); t.right(90)
# t.forward(100); t.right(90)
# t.forward(100); t.right(90)

# done() 必须写在最后一行：它启动事件循环，窗口才会保持显示
# 少了这一句，脚本执行完窗口会直接关掉（在 IDE 里表现为一闪而过）
turtle.done()
