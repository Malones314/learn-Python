# dictionary
# 列表是有序的对象集合，字典是无序的对象集合。类似于cpp中的map。
# 从Python 3.7开始，字典保持插入顺序，这意味着元素以它们被添加的顺序存储和访问。
# 字典中的键必须是唯一的，如果重复添加相同的键，后续的值会覆盖前面的值。
# 键必须是不可变类型，如整数、字符串、元组等。这是因为字典使用哈希表来实现，
# 而哈希表要求键必须是可哈希的，即不可变的。

"""
# 创建字典

# 使用花括号创建字典
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict2 = {'a': 2, 'b': 3, 'c': 4}

# 使用 dict() 函数创建字典
another_dict = dict(x=10, y=20, z=30)

# keys()：返回一个包含所有键的视图。
print(my_dict.keys())   #dict_keys(['a', 'b', 'c']) 
# values()：返回一个包含所有值的视图。
print(my_dict.values()) #dict_values([1, 2, 3])
# items()：返回一个包含所有键值对的视图。
print(my_dict.items())  #dict_items([('a', 1), ('b', 2), ('c', 3)])

# update(other_dict)：使用其他字典中的键值对更新当前字典。
my_dict.update(my_dict2) # dict_items([('a', 2), ('b', 3), ('c', 4)])

print(my_dict.pop('a')) #1 
print( my_dict.items()) #dict_items([('b', 2), ('c', 3)])

# 访问和修改字典

# 访问值
print(my_dict['a'])  # 输出: 1

# 修改值
my_dict['a'] = 100

# 添加新键值对
my_dict['d'] = 4

# 删除键值对
del my_dict['b']

print(my_dict)  # 输出: {'a': 100, 'c': 3, 'd': 4}

# 遍历字典

my_dict = {'a': 1, 'b': 2, 'c': 3}

# 遍历键
for key in my_dict:
    print(key)

# 遍历值
for value in my_dict.values():
    print(value)

# 遍历键值对
for key, value in my_dict.items():
    print(key, value)

"""
"""
# 列表推导式类似，字典推导式允许快速构建字典

# 构建一个字典，将字符串长度作为键，字符串作为值
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # 输出: {'apple': 5, 'banana': 6, 'cherry': 6}

"""
