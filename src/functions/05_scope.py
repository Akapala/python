"""第 5 课：变量的作用域

Python 找变量按这个顺序：局部 -> 嵌套 -> 全局 -> 内置（LEGB）。
- 局部作用域：函数内定义的变量，函数外访问不到
- 嵌套作用域：外层函数里的变量，内层函数能访问
- 全局作用域：不在任何函数里定义的变量
- 内置作用域：input / print / int 这些 Python 自带标识符

想在函数里改全局变量 -> 用 global 声明
想在内层函数里改外层（嵌套）变量 -> 用 nonlocal 声明

运行：
    python src/functions/05_scope.py
"""


def foo():
    b = 'hello'          # 局部变量

    def bar():
        c = True         # 嵌套作用域里的局部变量
        print(a)         # 能读到全局的 a
        print(b)         # 能读到外层 foo 的 b（嵌套作用域）
        print(c)

    bar()
    # print(c)  # NameError：c 只在 bar 里有效


def foo_global():
    global a             # 声明：要改的是全局的 a
    a = 200


if __name__ == '__main__':
    a = 100              # 全局变量
    foo()                # 输出 100 / hello / True

    # 不用 global 时，函数里的 a = 200 只是新建局部变量，改不到全局
    foo_global()
    print(a)             # 输出 200（因为用了 global）

    # 实际开发应尽量减少全局变量：作用域太广、生命周期太长，
    # 容易发生意料之外的修改，也增加代码间的耦合。
