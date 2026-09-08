def foo(a:int = 0,b:int = 1,c:int = 3) -> None:
    print(f"a: {a}, b: {b}, c: {c}")


def bar(*args:int) -> None:
    total = sum(args)
    print(f"total: {total}")
    print()


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo(1,2)
    print('call bar()')
    bar(1,2,3,4,5,6,7,8,9)