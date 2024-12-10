def Company(paramName):
    # 1. 创建空字典
    obj = {}

    # 2. 读取 __init__ 函数
    def __init__(self, name):
        self['name'] = name

    # 3. 调用 __init__ 函数
    __init__(obj, paramName)

    # 4. 抛出实例
    return obj


class Company2:

    def __init__(self, name):
        self.name = name



de = Company("Digit Engine")

print(de.items())

