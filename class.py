"""
Python 不支持多个构造函数，但可以通过在 __init__ 方法中使用默
认参数来实现类似的效果，根据不同的参数组合初始化对象的状态。
"""
class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is not None and arg2 is not None:
            # 根据两个参数初始化
            self.instance_variable1 = arg1
            self.instance_variable2 = arg2
        elif arg1 is not None:
            # 只根据一个参数初始化
            self.instance_variable1 = arg1
            self.instance_variable2 = "default_value"
        else:
            # 没有参数的默认初始化
            self.instance_variable1 = "default_value"
            self.instance_variable2 = "default_value"

    def display(self):
        return f"Instance variables: {self.instance_variable1}, {self.instance_variable2}"
# 不同的参数组合创建对象
obj1 = MyClass(1, 2)
obj2 = MyClass(3)
obj3 = MyClass()

# 调用方法显示对象状态
print(obj1.display())  # 输出：Instance variables: 1, 2
print(obj2.display())  # 输出：Instance variables: 3, default_value
print(obj3.display())  # 输出：Instance variables: default_value, default_value
