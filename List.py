#List
#支持字符、数字、字符串以及List（嵌套）
#加号（+）是连接操作，星号（*）是重复操作。
iList = [1,2,3,4,5] #创建list赋值
iList[-1] #访问iList最后一个怨怒是
sub_list = iList[1:3] #获取索引1到索引3的切片（不包含索引3）
sub_list = iList[2:] # 获取从索引2到末尾的元素
sub_list = iList[:3] # 获取从开头到索引3（不包括索引3）的元素
sub_list = iList[:] #获取所有元素

# append() 在列表末尾添加一个元素
# insert(a, b) 在list[a]处添加数值为b的元素
# extend(a)：使用列表a扩展当前列表
# pop(a) 删除并返回list[a]的元素，pop() 删除并返回最后一个元素
'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # 输出: [1, 2, 3, 4, 5, 6]

extend 和 append的区别：

# 使用 append() 方法
list1.append(list2)
print(list1)  # 输出: [1, 2, 3, [4, 5, 6]]

# 使用 extend() 方法
list1 = [1, 2, 3]
list1.extend(list2)
print(list1)  # 输出: [1, 2, 3, 4, 5, 6]


'''

# index()：返回第一个匹配元素的索引 返回整数类型的数据
# list.index(element, start, end)
'''
element：要查找的元素。
start（可选）：搜索的起始位置（包含）。默认值为 0。
end（可选）：搜索的结束位置（不包含）。默认值为列表的长度。
'''
'''
元素不在list中时，引发valueError异常
numbers = [1, 2, 3, 4, 5]
try:
    index_of_7 = numbers.index(7)
except ValueError:
    print("Element not found in the list.")
'''

"""
# 列表推导式
[expression for item in iterable if condition]
expression：要生成的元素，可以是任何表达式，包括函数调用和算术运算。
item：从iterable中逐个取出的元素。
iterable：可以是任何可迭代对象（如列表、元组、字符串等）。
condition（可选）：一个过滤条件，只有满足此条件的item才会被包含在生成的列表中。
"""
"""
# 带条件的列表推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # 输出: [0, 4, 16, 36, 64]
"""
"""
# 嵌套循环
combinations = [(x, y) for x in range(3) for y in range(3)]
print(combinations)  # 输出: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

#使用函数
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = [square(x) for x in numbers]
print(squared_numbers)  # 输出: [1, 4, 9, 16, 25]
"""

