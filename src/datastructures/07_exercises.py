"""第 7 课：综合练习 —— 用数据结构解决问题的套路

挑选了文档里最具代表性的 4 道练习，统一加上类型注解（与仓库严格检查一致）：
    1. generate_code  生成验证码        —— 字符串 + random
    2. get_suffix     取文件名后缀       —— 字符串 rfind
    3. max2           找最大和次大元素    —— 列表单次遍历
    4. which_day      算日期是一年第几天  —— 列表 + 闰年判断

文档里还有「双色球选号 / 约瑟夫环 / 井字棋」三个综合大案例，
以及「杨辉三角（嵌套列表）」「跑马灯」等练习，建议学有余力时自行拓展。

运行：
    python src/datastructures/07_exercises.py
"""
import random


def generate_code(code_len: int = 4) -> str:
    """生成由大小写字母和数字构成的随机验证码"""
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename: str, has_dot: bool = False) -> str:
    """取文件名的后缀名；has_dot 控制是否带点"""
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    return ''


def max2(x: list[int]) -> tuple[int, int]:
    """返回列表中最大的两个元素（只遍历一次）"""
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def is_leap_year(year: int) -> bool:
    """闰年：能被 4 整除但不能被 100 整除，或能被 400 整除"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year: int, month: int, date: int) -> int:
    """计算指定日期是这一年的第几天"""
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


if __name__ == '__main__':
    print('验证码:', generate_code(6))
    print('后缀(带点):', get_suffix('test.tar.gz', True))
    print('后缀(不带点):', get_suffix('test.tar.gz'))
    print('最大两个:', max2([3, 9, 1, 7, 5]))
    print('1980-11-28 是当年第', which_day(1980, 11, 28), '天')
