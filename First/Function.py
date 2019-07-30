# 函数


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(5))
print(fact(100))
# 调用太多层递归会导致栈溢出
# print(fact(1000))


# 栈溢出可以使用尾递归或循环优化。
def fact_wei(n):
    return fact_iter(n, 1)


def fact_iter(n, result):
    if n == 1:
        return result
    return fact_iter(n - 1, result * n)


# 遗憾的是Python编译器没有做尾递归优化，所以将函数改成尾递归方式，也还是会栈溢出
# print(fact_wei(1000))


# 汉诺塔
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)


# 调用
hanoi(5, 'A', 'B', 'C')
