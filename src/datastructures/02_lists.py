"""第 2 课：列表 list —— 最常用的容器

新知识点：
    * 列表是「有序、可变」的序列，元素可重复
    * 下标 / 切片（同字符串，支持负下标）
    * 增：append / insert / extend(或 +=)
    * 删：remove(按值, 不存在抛 ValueError) / pop(按下标) / clear
    * 遍历：下标循环、for elem in、enumerate 同时拿索引和值
    * 排序：sorted(返回新列表, 不改原列表) vs list.sort(原地改)
           key=len 可按字符串长度排序

运行：
    python src/datastructures/02_lists.py
"""


# ---- 创建与基本运算 ----
list1 = [1, 3, 5, 7, 100]
print(list1)
list2 = ['hello'] * 3
print(list2)                 # ['hello', 'hello', 'hello']
print(len(list1))            # 5

# ---- 下标运算（支持负下标）----
print(list1[0])              # 1
print(list1[-1])             # 100（倒数第 1 个）
print(list1[-3])             # 5

# ---- 修改元素 ----
list1[2] = 300
print(list1)                 # [1, 3, 300, 7, 100]

# ---- 三种遍历方式 ----
for index in range(len(list1)):      # 需要下标时
    print(index, list1[index])
for elem in list1:                   # 只要值
    print(elem)
for index, elem in enumerate(list1): # 索引 + 值都要
    print(index, elem)

# ---- 增删 ----
list1.append(200)            # 尾部追加
list1.insert(1, 400)         # 在位置 1 插入
list1 += [1000, 2000]        # 合并（等价于 extend）
print(list1)
if 3 in list1:               # remove 按值删，元素不存在会抛 ValueError
    list1.remove(3)
list1.pop(0)                 # 按下标删，返回被删元素
list1.pop(len(list1) - 1)
print(list1)
list1.clear()                # 清空
print(list1)                 # []

# ---- 切片：复制与反转 ----
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
fruits2 = fruits[1:4]       # 切片得到新列表
fruits3 = fruits[:]          # 完整切片 = 复制一份
fruits5 = fruits[::-1]       # 反向切片 = 反转
print(fruits2, fruits3, fruits5)

# ---- 排序：sorted vs sort ----
words = ['orange', 'apple', 'zoo', 'blueberry']
print(sorted(words))                 # 新列表，原列表不变
print(sorted(words, reverse=True))   # 降序
print(sorted(words, key=len))        # 按长度排
words.sort(reverse=True)             # 原地排序，改自身
print(words)
