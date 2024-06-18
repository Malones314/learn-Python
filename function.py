# 函数的定义使用 def 关键字，后面跟着函数名和参数列表。
# 函数体是缩进的代码块，用于执行函数定义的功能。
# 1:函数头部：包括 def 关键字、函数名和参数列表。
# 2:函数体：缩进的代码块，包含函数的具体实现。
# 3:返回值：使用 return 语句返回函数的结果（可选）。
def hello(name):
  print( f"hello, {name}")
# 参数类型
"""
# 默认参数
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Bob")  # 输出: Hello, Bob!
greet("Charlie", "Hi")  # 输出: Hi, Charlie!
"""

"""
# 可变长参数
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4)
print(result)  # 输出: 10

"""
"""
# 关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)  # 输出:
# name: Alice
# age: 30

"""