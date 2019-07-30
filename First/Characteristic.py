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

