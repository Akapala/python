"""第 3 课：推导式与生成器 —— 空间与时间的权衡

新知识点：
    * 列表推导式 [表达式 for ... in ...]：创建时就把所有结果算好放进内存
    * 生成器表达式 (表达式 for ... in ...) ：惰性，用到才算，几乎不占内存
    * sys.getsizeof 查看对象占用字节数
    * yield 把普通函数变成生成器函数（每次执行到 yield 就“暂停”交出一个值）

运行：
    python src/datastructures/03_generators.py
"""
import sys


# ---- 列表推导式：一次性算完，占内存 ----
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))      # 列表本身占的字节数（元素都已就绪）

# ---- 生成器表达式：只记住“怎么算”，几乎不占内存 ----
g = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(g))      # 比上面的列表小得多
# 生成器本身不存数据，要取才现算：
for _ in g:
    pass                    # 真正计算发生在这里

# ---- yield 生成器函数：斐波那契数列 ----
def fib(n: int):
    """生成前 n 个斐波那契数（用 yield 逐个交出，不一次性占内存）"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    for val in fib(20):
        print(val)
