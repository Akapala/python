"""第 6 课：字典 dict —— 键值对映射

新知识点：
    * 字典用 {键: 值} 或 dict() 创建，键唯一、无序
    * 取值：d[key]（没有会 KeyError） / d.get(key, 默认值)（更安全）
    * 遍历：默认遍历键；items() 同时拿键值对
    * 增改：d[key] = 值；update(批量)
    * 删：pop(key) / popitem() / clear()
    * 字典推导式：{k: v for ...}

运行：
    python src/datastructures/06_dicts.py
"""


# ---- 创建 ----
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
items1 = dict(one=1, two=2, three=3, four=4)
items2 = dict(zip(['a', 'b', 'c'], '123'))   # zip 把两个序列“拉链”成对
items3 = {num: num ** 2 for num in range(1, 10)}  # 字典推导式
print(items1, items2, items3)

# ---- 取值 ----
print(scores['骆昊'])
for key in scores:                      # 默认遍历“键”
    print(f'{key}: {scores[key]}')
for key, value in scores.items():       # items() 同时拿键值
    print(key, value)

# ---- 增改 ----
scores['白元芳'] = 65                    # 有则改，无则增
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)

# ---- 安全取值：get 可设默认值 ----
print(scores.get('武则天'))              # None（键不存在不报错）
print(scores.get('武则天', 60))          # 60（默认值）

# ---- 删除 ----
print(scores.pop('骆昊', 100))           # 删键并返回值，给默认防 KeyError
print(scores.popitem())                  # 删“最后”插入的键值对
scores.clear()
print(scores)                           # {}
