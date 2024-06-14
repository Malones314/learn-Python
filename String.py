# String
# 由数字、字母、下划线组成的串
# 加号（+）是字符串连接运算符，星号（*）是重复操作。
# 可以使用'或者"来创建字符串。
# python中不支持单个字符，单个字符也是作为一个字符串来使用。
# 引号前小写的"u"表示这里创建的是一个 Unicode 字符串。
####################################################################################
c = u "你好"
####################################################################################
# in :在字符串中，not in ：不在字符串中
####################################################################################
c = "123"
b = "456"
c+=b
print("3" in c)   #True
print("7" in c)   #True
####################################################################################
# 支持负索引，负索引会简单的与字符串长度相加
# c[-1]和c[len(c)-1]相同
# 字符串的值不可改变，如果需要修改字符串的值，通常需要创建一个新的字符串。
# replace() 返回一个新的字符串，其中的某些子字符串被替换。

my_string = r'C:\Users' #原始（raw）字符串字面量，即去除反斜杠转义机制
print(my_string)    #输出C:\Users

"""
my_string = "123123"
new_string = my_string.replace("1", "x")
print(new_string)  # 输出: x23x23
"""
"""
original_string = "1234567"
new_string = original_string[:3] + "x" + original_string[4:]
print(new_string)  # 输出: 123x567
"""
#使用byte_array来修改字符串，用于处理二进制数据和需要对字节进行修改的场景

"""
my_string = "Hello, World!"
byte_array = bytearray(my_string, 'utf-8')

# 修改单个字节
byte_array[0] = ord('h')  # 将 'H' 修改为 'h'
#byte_array[0] = b'h'错误，bytearray 的元素必须是整数，应该使用对应字符的ASCII值。
print(byte_array)  # 输出: bytearray(b'hello, World!')

# 修改一段字节
byte_array[7:12] = b'Python'
print(byte_array)  # 输出: bytearray(b'hello, Python!')

my_string = byte_array.decode("utf-8")    #将 bytearray 转换回字符串
print(my_string)
"""