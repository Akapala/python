"""第 3 课：可变参数 *args

当「到底接收几个参数」由调用者决定、函数设计者事先不知道时，
用参数名前加 * 的可变参数，它会把所有位置参数收进一个元组。

运行：
    python src/functions/03_variable_args.py
"""


def add(*args:int):
    """对传入的任意多个数求和"""
    total = 0
    for val in args:
        total += val
    return total


if __name__ == '__main__':
    # 可以传入 0 个、1 个、多个参数
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(1, 3, 5, 7, 9))

    # 进阶（后面「函数式」再展开）：用内置 sum() 一行就能写完
    # print(sum(args))
