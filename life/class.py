    # 1. 声明 5 个学生并做一个查看方法，调用方法可以打印出所有学生信息 “姓名+工号+工资”
    # 2. 提供方法查看所有员工工资总和
    # 3. 提供方法，给予一个工号帮助查看对应员工信息 “姓名+工号+工资”
    # 4. 提供方法，输入一个工号，对应工号员工离职


class Employee:
    '所有员工的基类'
    empList = []

    def __init__(self, name, workNo, salary):
        self.name = name
        self.workNo = workNo
        self.salary = salary
        Employee.empList.append(self)

    def displayCount(self):
        return "Total Employee %d" % len(Employee.empList)



count = Employee('小明', 376521, '1000.00').displayCount()
print(count)
