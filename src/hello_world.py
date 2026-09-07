for n in range(2, 101):
    for d in range(2, n):        # 挨个试除
        if n % d == 0:
            break                 # 找到因子 → 合数，跳出
    else:
        print(n, end=" ")         # 内层循环跑完都没 break → 素数
# 2 3 5 7 11 13 ... 97