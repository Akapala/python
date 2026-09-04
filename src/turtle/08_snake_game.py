"""第 8 课：综合项目 —— 贪吃蛇

把前面 7 课的家伙事儿全用上：列表、函数、循环、条件、事件、计时器。

玩法：方向键或 WASD 控制，吃到红色方块加一分，撞墙或撞到自己就重来。

新知识点：
    * 列表当队列用：蛇身是一串 turtle，每帧从尾巴往头逐个「接位」
    * screen.ontimer(函数, 毫秒)：注册一个定时回调，实现游戏主循环
    * 把方向存在对象属性里：head.direction = "up"（Python 允许动态加属性）
    * 网格坐标：所有位置都对齐到 CELL 的整数倍，碰撞判断才能用 distance 简单搞定

运行：
    python src/turtle/08_snake_game.py
"""

import random
import turtle

CELL = 20                       # 一格 20 像素
WIDTH, HEIGHT = 620, 620
BOUND = WIDTH // 2 - CELL * 3   # 可活动的边界：留出边距，顶部还要留给计分板
DELAY = 110                     # 每帧间隔毫秒，越小越快

screen = turtle.Screen()
screen.title("08 贪吃蛇")
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.tracer(0)                # 游戏画面自己控制刷新，关掉自动动画

# --- 蛇头 ---
head = turtle.Turtle("square")  # 形状用 "square"，天然就是一格
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"         # 给对象临时挂一个属性，记录当前方向

# --- 蛇身：每吃一个食物就 append 一节 ---
segments = []

# --- 食物 ---
food = turtle.Turtle("square")
food.color("red")
food.penup()
food.goto(CELL * 4, CELL * 3)

# --- 计分板 ---
pen = turtle.Turtle()
pen.hideturtle()                # 只写字，不显示这支笔
pen.color("white")
pen.penup()
pen.goto(0, HEIGHT // 2 - 30)   # 贴在画布顶部，避开蛇的活动区域

score = 0
best = 0


def show_score():
    """刷新计分板。write 之前必须 clear，否则文字会层层叠在一起。"""
    pen.clear()
    pen.write(
        f"得分：{score}   最高：{best}   |   方向键 / WASD 移动",
        align="center",
        font=("Microsoft YaHei", 13, "normal"),
    )


def go_up():
    if head.direction != "down":      # 禁止 180 度掉头，否则会直接撞上自己的脖子
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move_head():
    """根据当前方向，把蛇头挪动一整格。"""
    if head.direction == "up":
        head.sety(head.ycor() + CELL)
    elif head.direction == "down":
        head.sety(head.ycor() - CELL)
    elif head.direction == "left":
        head.setx(head.xcor() - CELL)
    elif head.direction == "right":
        head.setx(head.xcor() + CELL)


def follow():
    """蛇身跟随：从最后一节开始，每节挪到它前面一节的位置。

    顺序必须是「从尾到头」，如果从头开始挪，前一节的位置已经被覆盖，
    后面几节就全都叠在一起了。
    """
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())


def move_food():
    """把食物随机挪到一个网格点上。randrange 的步长参数保证对齐格子。"""
    x = random.randrange(-BOUND, BOUND + CELL, CELL)
    y = random.randrange(-BOUND, BOUND + CELL, CELL)
    food.goto(x, y)


def add_segment():
    """吃到食物：在蛇尾追加一节。"""
    new = turtle.Turtle("square")
    new.color("gray")
    new.penup()
    if segments:
        new.goto(segments[-1].position())
    else:
        new.goto(head.position())
    segments.append(new)


def reset():
    """撞墙或撞到自己：清场重来。"""
    global score
    head.goto(0, 0)
    head.direction = "stop"
    for seg in segments:
        seg.goto(1000, 1000)   # 挪到画布外面，视觉上等于消失
    segments.clear()           # 清空列表，注意不是 seg = []
    score = 0
    show_score()


def game_loop():
    """一帧的逻辑。末尾用 ontimer 再约一次自己，就形成了游戏主循环。"""
    global score, best

    follow()        # 1. 身体先跟上
    move_head()     # 2. 头再动

    # 3. 撞墙判定
    if abs(head.xcor()) > BOUND or abs(head.ycor()) > BOUND:
        reset()
        screen.update()
        screen.ontimer(game_loop, DELAY)
        return

    # 4. 撞到自己判定
    for seg in segments:
        if head.distance(seg) < CELL / 2:
            reset()
            screen.update()
            screen.ontimer(game_loop, DELAY)
            return

    # 5. 吃到食物
    if head.distance(food) < CELL / 2:
        add_segment()
        move_food()
        score += 1
        best = max(best, score)
        show_score()

    screen.update()
    screen.ontimer(game_loop, DELAY)   # 约下一帧，游戏就一直跑下去


# ---- 事件绑定 ----
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

show_score()
game_loop()       # 启动第一帧
turtle.done()     # 进入事件循环；真正的循环由 ontimer 维持
