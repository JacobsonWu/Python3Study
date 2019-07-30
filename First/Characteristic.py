from collections import Iterable

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
