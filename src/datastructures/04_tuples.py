"""第 4 课：元组 tuple —— 不可变的序列

新知识点：
    * 元组用 () 定义，元素不能修改（不可变对象）
    * 遍历用 for ... in（循环变量名随意，不叫 member 也行）
    * 元组 -> 列表 list()、列表 -> 元组 tuple() 互相转换
    * 为什么还要元组：不可变更安全（线程安全）、创建更快、占用更小
    * 函数返回多个值时，本质就是返回一个元组

运行：
    python src/datastructures/04_tuples.py
"""


# ---- 定义与访问 ----
t = ('骆昊', 38, True, '四川成都')
print(t)
print(t[0])                 # 取元素
print(t[3])

# ---- 遍历（循环变量名随便取）----
for member in t:
    print(member)

# ---- 不能改元素（取消下一行注释会 TypeError）----
# t[0] = '王大锤'

# 想“改”？只能让变量重新引用一个新元组（旧元组等垃圾回收）
t = ('王大锤', 20, True, '云南昆明')
print(t)

# ---- 与列表互转 ----
person = list(t)            # 元组 -> 列表（列表可改）
person[0] = '李小龙'
person[1] = 25
print(person)
fruits_tuple = tuple(['apple', 'banana', 'orange'])  # 列表 -> 元组
print(fruits_tuple)
