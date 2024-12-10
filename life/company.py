class Company:
    # 实例化函数
    def __init__(self, name, emp_list=[]):
        self.name = name
        self.emp_list = emp_list
# 打印格式化函数

    def __str__(self):
        display_str_list = []
        for emp in self.emp_list:
            # display_str_list.append(f'{emp["workNo"]} "{emp["name"]}" {emp["age"]}')
            display_str_list.append(
                f'{emp["workNo"]} "{emp["name"]}" {emp["age"]}')
        return '\n'.join(display_str_list)
# 输入一个名字打印出对应的员工信息

    def find_names(self, name):
        display_str = []
        for emp in self.emp_list:
            if emp["name"] == name:
                display_str.append(
                    f'{emp["workNo"]} "{emp["name"]}" {emp["age"]}')
        return ''.join(display_str)

    def find_name(self, name):
        for emp in self.emp_list:
            if emp["name"] == name:
                return f'{emp["workNo"]} "{emp["name"]}" {emp["age"]}'


de = Company('Digital Engine',
             [{'workNo': '37072', 'age': 20, 'name': 'John Doe'}, {'workNo': '37072', 'age': 200, 'name': 'John Doe'}, {'workNo': '372417', 'age': 21, 'name': 'Mike Lane'}, {'workNo': 'WB27417', 'age': 21, 'name': 'James Lu'}, {'workNo': 'WB17417', 'age': 18, 'name': 'X Murphy'}, {'workNo': '741722', 'age': 32, 'name': 'Gone Luluya'}
              ])


# print(de.find_name('John Doe'))


x = ['a', 'b', 'c']

print(range(len(x)))
