from collections import Iterable
import os

# 获取list或tuple的部分元素
l = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 切片, 获取l中索引index满足 1 <= index < 3的部分元素
sub = l[1:3]
print(sub)
# 切片中如果第一个所以为0，可以省略
print(l[:3])
# python也支持负数切片
print(l[-3: -1])
# 如果切片到最后一个元素，也可以省略
print(l[-3:])
print(l[1:])

l = list(range(100))
# 取出前10个数
print(l[:10])
# 后10个数
print(l[-10:])
# 取出第10-20个数
print(l[10:20])
# 取前10个数，每两个数取一个
print(l[:10:2])
# 取所有数，每五个数取一个
print(l[::5])
# 什么都不写，复制一个list
print(l[:])
# 字符串也可以切片，相当于java substring方法
s = "ABCDEF"
print(s[:3])

# 迭代, Python的迭代是可以用于任何可以迭代的对象上
# 迭代list
l = [1, 2, 3, 4]
for item in l:
    print(item)
print("")

# 迭代 tuple
t = (2, 3, 5, 6, "Hello")
for item in t:
    print(item)
print("")

# 迭代dict key
dict = {"a": 3, "b": 4, "c": "world"}
for key in dict:
    print(key)
print("")

# 迭代dict值
for value in dict.values():
    print(value)
print("")

# 迭代dict key-value
for item in dict.items():
    print(item[0], "=", item[1])
print("")

# 字符串也是可迭代对象
for c in "ABCD":
    print(c)
print("")

# 通过collections模块的Iterable类型判断是否是可迭代对象
print(isinstance(dict, Iterable))
print(isinstance("ABC", Iterable))
print(isinstance(123, Iterable))

# 使用enumerate来提供下标
for index, value in enumerate(dict.items()):
    print(index, value)
print("")

# for里同时引用两个变量在Python中是很常见的
for a, b in [(1, 2), (3, 4), (5, 6)]:
    print(a, b)
print("")


# 查找最大值和最小值，返回tuple (min, max)
def findMinAndMax(list=None):
    if list is None or len(list) == 0:
        return None, None
    minvalue = list[0]
    maxvalue = list[0]
    for i, val in enumerate(list):
        if i > 0:
            if minvalue > val:
                minvalue = val
            if maxvalue < val:
                maxvalue = val

    return minvalue, maxvalue


v = findMinAndMax([8, -1, 1, 232, 34, 42, 5, 5])
print(v)

# 列表生成式
# 生成 [1x1,2x2,3x3....10x10]list
a = [x * x for x in range(1, 11)]
print(a)

# 可以加上条件判断，仅生成偶数
a = [x * x for x in range(1, 11) if x & 1 == 0]
print(a)

# 可以使用两层循环,三层及以上就很少用了
a = [m + n for m in "ABC" for n in "XYZ"]
print(a)

# 列出当前目录下的所有文件和目录名
dirs = [d for d in os.listdir('.')]
print(dirs)

# 列表式也能使用两个变量来生成list，比如迭代 dict
dict = {"x": "A", "y": "B", "z": "C"}
a = [k + " = " + v for k, v in dict.items()]
print(a)

# 把所有的大写字母转小写
l = ["Hello", "World", "IBM", "Apple"]
a = [s.lower() for s in l]
print(a)

# 把所有的大写字母转小写,数字没有lower方法会报错。
l = ["Hello", "World", "IBM", "Apple", 18]
a = [s.lower() if isinstance(s, str) else s for s in l]
print(a)

# 生成器，只要把列表生成式[]改成()就是一个生成器
g = (x for x in range(1, 10) if x & 1)
print(g)
# 使用next获取,没有下一个元素会抛出StopIteration异常
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
print("")

g = (x for x in range(1, 10) if x & 1)
# 使用for迭代，因为生成器g也是可迭代的
for x in g:
    print(x)
# 迭代后或使用next到最后，生成器再迭代就没有了。已经指向最后一个值
# for x in g:
#     print(x)

print("==feb==")


# 使用函数方式生成生成器


# 定义一个打印斐波拉契数列的方法
def feb(m):
    n, x, y = 0, 0, 1
    while n < m:
        print(y)
        x, y = y, x + y
        n = n + 1
    return 'done'


feb(5)


# 只要把print(y) 改成 yield y就可以了
def feb_for_generator(m):
    n, x, y = 0, 0, 1
    while n < m:
        yield y
        x, y = y, x + y
        n = n + 1
    return 'done'


g = feb_for_generator(5)
print(g)
for a in g:
    print(a)


# 函数和generator的流程不一致，函数是顺序执行，generator是每次遇到 yield 返回，等到下一次next继续执行
def test_generator():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield (2, 3)
    print("step 4")
    yield 'end'


g = test_generator()
print(g)
print('invoke next 1')
print("ret = ", next(g))
print('invoke next 2')
print("ret = ", next(g))
print('invoke next 3')
print("ret = ", next(g))
print('invoke next 4')
print("ret = ", next(g))

# 获取生成器方法返回值 必须捕获StopIteration来获取
g = feb_for_generator(5)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print('return value is ', e.value)
        break


# 杨辉三角每一行数据的生成器
def triangles():
    line = 1
    tri = [1]
    while True:
        yield tri
        line = line + 1
        tri = tri[:]
        tri.append(1)
        for i in range((line - 1) // 2, 0, -1):
            tri[i] = tri[i] + tri[i - 1]
            tri[-i - 1] = tri[i]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

