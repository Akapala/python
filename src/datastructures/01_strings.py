"""第 1 课：字符串 —— 文本的基本操作

新知识点：
    * 拼接 + 与重复 *
    * 成员运算 in / not in
    * 下标 [] 与切片 [start:end:step]（含负下标、反向切片 [::-1]）
    * 转义字符 \\n \\t \\' \\\\ 与原始字符串 r'...'
    * 常用方法：len / find / startswith / strip / upper ...
    * 三种格式化：% 占位符、str.format、f-string（最推荐）

运行：
    python src/datastructures/01_strings.py
"""


# ---- 1. 拼接、重复、成员运算 ----
s1 = 'hello ' * 3
print(s1)                 # hello hello hello
s2 = 'world'
s1 += s2
print(s1)                 # hello hello hello world
print('ll' in s1)         # True
print('good' in s1)       # False

# ---- 2. 下标与切片 ----
text = 'abc123456'
print(text[2])            # c
print(text[2:5])          # c12
print(text[2:])           # c123456
print(text[2::2])         # c246
print(text[::2])          # ac246
print(text[::-1])         # 654321cba  反向切片 = 字符串反转
print(text[-3:-1])        # 45

# ---- 3. 转义与原始字符串 ----
print('\'hello, world!\'')        # 用 \' 表示单引号
print('\n\\hello\\\n')            # \n 换行 \\ 反斜杠
print(r'\n\\hello\\\n')           # 原始字符串：反斜杠不当转义

# ---- 4. 常用方法 ----
str1 = 'hello, world!'
print(len(str1))                 # 13
print(str1.capitalize())         # Hello, world!
print(str1.title())              # Hello, World!
print(str1.upper())              # HELLO, WORLD!
print(str1.find('or'))           # 8
print(str1.find('shit'))         # -1（找不到返回 -1，不会抛异常）
print(str1.startswith('hel'))    # True
print(str1.endswith('!'))        # True
str3 = '  jackfrued@126.com '
print(str3.strip())              # 去掉两侧空白

# ---- 5. 三种格式化（推荐 f-string）----
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))        # 老式 % 占位符
print('{0} * {1} = {2}'.format(a, b, a * b)) # str.format
print(f'{a} * {b} = {a * b}')                # f-string（最简洁）
