"""第 6 课：事件回调 —— 做一个能用鼠标画画的画板

前面 5 课的程序都是「写好剧本，从头演到尾」。
这一课反过来：程序等着你来操作，你点什么、按什么键，它才做什么。

新知识点：
    * 回调函数：把「函数本身」当作参数传进去（传名字，不要加括号）
    * ondrag()：鼠标拖拽事件；onkey()：键盘事件
    * global：在函数内部修改模块层的变量，必须先声明 global
    * 闭包/工厂函数：用一个函数生成另一个函数，绕开 onkey 不能传参的限制

操作说明：
    左键拖拽        画线
    1 ~ 5          换颜色
    u              抬笔 / 落笔切换
    + / -          加粗 / 减细
    c              清屏

运行：
    python src/turtle/06_click_board.py
"""

import turtle

# 模块层变量 = 整个程序共享的状态
COLORS = {"1": "black", "2": "red", "3": "green", "4": "blue", "5": "purple"}
is_first_drag = True       # 第一次拖拽要「跳过去」而不是「画过去」

screen = turtle.Screen()
screen.title("06 画板：拖拽画线 | 1-5 换色 | u 抬笔 | +/- 粗细 | c 清屏")
screen.setup(900, 650)
screen.bgcolor("white")
# 交互程序不能用 tracer(0)：那样必须手动 update() 才看得到，你画的东西不会实时出现

t = turtle.Turtle()
t.speed(0)
t.width(3)


def draw(x, y):
    """鼠标拖拽时反复触发：把画笔跟到鼠标当前位置。"""
    global is_first_drag
    if is_first_drag:
        # 画笔初始停在画布中心 (0,0)。第一次拖拽如果直接 goto，
        # 会从中心拉出一条长直线，所以第一次只移动、不画。
        t.penup()
        t.goto(x, y)
        t.pendown()
        is_first_drag = False
    else:
        t.goto(x, y)


def make_color_setter(color):
    """返回一个「把画笔换成指定颜色」的函数。

    onkey(函数, 按键) 要求这个被注册的函数不能带参数，
    可 set_color(color) 明明需要参数。解决办法：让外层函数记住 color，
    内层函数 setter 再去用它——这就是闭包。
    """
    def setter():
        t.pencolor(color)
    return setter


def toggle_pen():
    """按 u：在抬笔 / 落笔之间切换。isdown() 用来查询当前是否在画线。"""
    global is_first_drag
    if t.isdown():
        t.penup()
    else:
        t.pendown()
        is_first_drag = True   # 重新落笔时，下一次拖拽仍然要先「跳过去」


def thicker():
    t.width(t.width() + 2)


def thinner():
    t.width(max(1, t.width() - 2))   # max 保证笔宽不会变成 0 或负数


def clear_all():
    t.clear()   # 只擦掉这支笔画过的痕迹，不动背景色


# ---- 事件绑定：全部传「函数名字」，绝对不能加括号 ----
# 写 t.ondrag(draw()) 是错的：那会当场调用一次 draw，然后把返回值 None 注册进去
t.ondrag(draw)

screen.listen()            # 打开键盘监听，少了这句 onkey 全部失效
for key, color in COLORS.items():
    screen.onkey(make_color_setter(color), key)
screen.onkey(toggle_pen, "u")
screen.onkey(thicker, "plus")
screen.onkey(thinner, "minus")
screen.onkey(clear_all, "c")

turtle.done()   # 进入事件循环，程序停在这一行等你操作
