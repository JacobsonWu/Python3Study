# ========================================基础↓=========================================
a = 100
if a >= 1:
    print(a, '是正数')
else:
    print(a, '是负数')
# 转义
print("I'm \"OK\"")
print('I\'m ok.\\\n\\\t\\')
# r表示''内部不转义
print(r'\\\\t\\')
# 多行输出
print('''line1
     line2
     line3 ''')
# 布尔值
print(True)
print(False)
print(3 > 2)
print(3 < 2)

# 与
print(True and False)
# 或
print(True or False)
# 非
print(not True)
print(not 1 > 2)

a = 1
if not a > 2:
    print(a, 'is not bigger 2')
else:
    print(a, 'is bigger 2')
print(None)

# Python是动态语言
# a是整型
a = 1
print(a)
# a变成了字符串
a = '变成了字符串'
print(a)

a = "ABC"
b = a
a = "XYZ"
print(a)
print(b)

# 通常用全部大写表示常量，但Python中没有真正的常量，还是可以改变他的值。全部大写是一个常用的规范
PI = 3.1415926
print(PI)

# 整数除法后为浮点数
a = 10 / 3
print(a)
a = 6 / 3
print(a)
# 地板除，取整数部分
a = 10 // 3
print(a)
a = 6 // 3
print(a)
# 取模,取余数
print(7 % 3)
print(1209320392039023902342323232323232323232323232323232323920392323 *
      2093290322323232323232323110302938023802323232323)
print("可以输出中文，Python使用Unicode编码")
# 字符转整数表示
print(ord("A"))
print(ord("中"))
# 整数表示转字符
print(chr(65))
print(chr(20013))
# 也可以用16进制编码表示
print('\u4e2d\u6587')
# b前缀表示转为byte数组
x = b'ABC'
print(x)
# x = b''转成byte只支持小于255的字符 bytes can only contain ASCII literal characters.
# x = b'中文'
# 指定编码
print("中文C".encode('UTF-8'))
print("ABC".encode("ASCII"))
# 中文无法转ascii
# print("中文".encode("ascii"))
# 忽略无效的字节
x = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(x)
# 计算字符长度
print(len(x))
print(len('ABC'))
print(len('中文'))
# 计算字节数组长度
print(len(b'ABC'))
print(len('中文'.encode('utf8')))
# 格式化也是使用%来
print("%s: %d + %f = %f or %x(16进制)" % ('算式', 5, 7, 5 + 7, 5 + 7))
print('%2d-%02d' % (3, 1))
# 输出保留两位小数
print('%.2f' % 3.1415926)
# %s永远器作用，可以用与任何数据类型
print("Age: %s, Name: %s, Boy: %s" % (16, 'Yang', True))
# %如果是个普通字符，用%转义
print("growth rate is %d%%" % 6)
# 是用format格式化
print("Hello, {0}, 你的成绩提高了{1:.1f}%".format('小明', 17.232))