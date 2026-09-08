"""第 2 课：函数的参数 —— 默认参数与关键字实参

Python 函数参数可以有默认值，也支持用「参数名=值」的关键字方式传参。
因为有默认参数 + 可变参数，Python 不需要像 C++ 那样支持函数重载，
一个函数就能有多种调用方式。

运行：
    python src/functions/02_params.py
"""

from random import randint


def roll_dice(n:int=2):
    """摇 n 颗色子，返回点数总和（默认摇 2 颗）"""
    total:int = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a:int=0, b:int=0, c:int=0):
    """三个数相加，参数都有默认值"""
    return a + b + c


if __name__ == '__main__':
    # 不传参 -> 使用默认值
    print(roll_dice())        # 摇 2 颗
    print(roll_dice(3))       # 摇 3 颗

    # add 的多种调用方式，效果等价于 C++ 的函数重载
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    # 关键字实参：可以不按参数定义的顺序传
    print(add(c=50, a=100, b=200))
