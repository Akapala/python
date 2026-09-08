"""第 6 课：综合练习 —— 把函数组合起来解决问题

文档给出的 4 道练习题。核心思想：把重复 / 独立的功能抽成函数，
再用函数组合解决更复杂的问题。

练习1：最大公约数 gcd / 最小公倍数 lcm
练习2：判断回文数 is_palindrome
练习3：判断素数 is_prime
练习4：判断回文素数（组合上面两个函数）

运行：
    python src/functions/06_exercises.py
"""

import math
def gcd(x:int, y:int) -> int:
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1

def lcm(x:int, y:int) -> int:
    """求最小公倍数"""
    return x * y // gcd(x, y)


def is_palindrome(num:int):
    """判断一个数是不是回文数（正着读反着读一样）"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


def is_prime(num:int) -> bool:
    """判断一个数是不是素数"""
    for factor in range(2, math.isqrt(num) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == '__main__':
    # 练习1
    print('gcd(12, 18) =', gcd(12, 18))
    print('lcm(12, 18) =', lcm(12, 18))

    # 练习2
    print('12321 是回文数?', is_palindrome(12321))
    print('12345 是回文数?', is_palindrome(12345))

    # 练习3
    print('2 是素数?', is_prime(2))
    print('9 是素数?', is_prime(9))

    # 练习4：回文素数 —— 组合两个已有函数
    num = int(input('请输入一个正整数: '))
    if is_palindrome(num) and is_prime(num):
        print(f'{num} 是回文素数')
    else:
        print(f'{num} 不是回文素数')
