"""第 1 课：定义函数 —— 把重复代码抽成函数

背景：算组合数 C(M, N) = M! / (N! * (M-N)!)。
原题代码把「求阶乘」的循环写了 3 遍，这是最坏的代码味道——重复。
编程名言（Martin Fowler）：代码有很多种坏味道，重复是最坏的一种。

这节课我们把求阶乘封装成 fac() 函数，需要的时候直接调用。

运行：
    python src/functions/01_factorial.py
"""


def fac(num:int):
    """求 num 的阶乘（num!）"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


# ---- 用函数重构后的 C(M, N) 计算：不再手写三次循环 ----
if __name__ == '__main__':
    m = int(input('m = '))
    n = int(input('n = '))
    print(fac(m) // fac(n) // fac(m - n))

    # 小提示：Python 标准库 math 里已有 factorial，
    # 真实项目直接用 from math import factorial 即可，不必自己造轮子。
