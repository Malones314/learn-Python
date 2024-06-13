# Tuple
# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
# 元组不允许更新，而列表允许更新。

'''
# 创建包含一些整数的元组
numbers = 5, 3, 2,1,4
numbers[0] = 3  #error，元组创建后不可更改

# 创建空元组
empty_tuple = ()
empty_tuple = 1, 2, 3 #no error
empty_tuple[0] = 2  #error 不能更改

# 创建包含不同类型元素的元组
mixed_tuple = (1, "Hello", 3.14, True)
'''

# 和list一样有切片功能，用于获取元组的一个子集
'''
numbers = (1, 2, 3, 4, 5)

# 获取从索引1到索引3（不包括索引3）的元素
sub_tuple = numbers[1:3]  # (2, 3)

# 获取从索引2到末尾的元素
sub_tuple = numbers[2:]  # (3, 4, 5)

# 获取从开头到索引3（不包括索引3）的元素
sub_tuple = numbers[:3]  # (1, 2, 3)

# 获取所有元素
sub_tuple = numbers[:]  # (1, 2, 3, 4, 5)

'''

'''
numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number)

# 输出:
# 1
# 2
# 3
# 4
# 5
'''

# 元组的应用场景
# 由于元组的不可变性，它们适用于一些特定的场景：
  #不可变数据：需要保证数据不可变时使用元组，例如作为字典的键。
  #多值返回：函数返回多个值时可以使用元组。
  #固定集合：需要存储固定数量的元素时，元组更为合适。

'''
#多值返回实例：

def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([1, 2, 3, 4, 5])
print(result)  # 输出: (1, 5)

min_value, max_value = result
print(min_value)  # 输出: 1
print(max_value)  # 输出: 5

'''  