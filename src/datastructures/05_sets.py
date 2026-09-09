"""第 5 课：集合 set —— 去重 + 集合运算

新知识点：
    * 集合用 {} 或 set() 创建，元素不重复、无序
    * 增：add(单个) / update(批量)
    * 删：discard(没有也不报错) / remove(没有就 KeyError) / pop(随机删一个)
    * 运算：交集 & 、并集 | 、差集 - 、对称差 ^
    * 子集 / 超集：<= 、>=

运行：
    python src/datastructures/05_sets.py
"""


# ---- 创建（自动去重）----
set1 = {1, 2, 3, 3, 3, 2}
print(set1)                 # {1, 2, 3}
print('Length =', len(set1))
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 集合推导式
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# ---- 增删 ----
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)             # 没有 5 也不报错
if 4 in set2:               # remove 删不到会抛 KeyError，先判断更稳
    set2.remove(4)
print(set1, set2)
print(set3.pop())           # 随机弹出一个（集合无序）
print(set3)

# ---- 集合运算 ----
print(set1 & set2)          # 交集
print(set1 | set2)          # 并集
print(set1 - set2)          # 差集：在 set1 不在 set2
print(set1 ^ set2)          # 对称差：只在一个里
print(set2 <= set1)         # 是否子集
print(set1 >= set3)         # 是否超集
