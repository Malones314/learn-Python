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

# index()：返回第一个匹配元素的索引
# list.index(element, start, end)
'''
element：要查找的元素。
start（可选）：搜索的起始位置（包含）。默认值为 0。
end（可选）：搜索的结束位置（不包含）。默认值为列表的长度。
'''
