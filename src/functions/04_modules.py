"""第 4 课：模块与 __main__ 守卫

一个 .py 文件就是一个模块（module）。把函数放进不同模块，
就能解决「多人协作时同名函数冲突」——通过 import 区分来源。

关键技巧：模块里如果写了会直接执行的代码，
要用 if __name__ == '__main__': 包起来。
这样「被别人 import 时不会乱跑，只有自己被直接运行时才执行」。

运行：
    python src/functions/04_modules.py
"""


def foo():
    print('hello, world!')


def bar():
    print('goodbye, world!')


# ---- 推荐的代码骨架：执行逻辑收进 main()，再用守卫调用 ----
def main():
    foo()
    bar()


if __name__ == '__main__':
    # 只有「直接运行本文件」时 __name__ 才是 '__main__'
    # 被别的文件 import 时，这段不会执行
    main()

# ---- 关于同名函数的小坑（了解即可）----
# Python 没有函数重载，后面定义的同名函数会覆盖前面的：
#   def foo(): print('A')
#   def foo(): print('B')   # foo 现在指向 B，A 被覆盖
# 解决：把不同 foo 放进 module1.py / module2.py，
#   from module1 import foo   -> 输出 A
#   from module2 import foo   -> 输出 B
# 注意：连续 from module1 import foo; from module2 import foo 时，
# 后者会覆盖前者（最后导入的生效）。
