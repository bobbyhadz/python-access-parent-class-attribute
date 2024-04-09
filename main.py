# Accessing parent class attributes in Python

class Employee():
    cls_id = 'emp-cls'

    def __init__(self, name):
        self.salary = 100
        self.name = name


class Developer(Employee):
    def __init__(self, name):
        # 👇️ invoke parent __init__() method
        super().__init__(name)

        # 👇️ accessing parent instance variable
        print(self.salary)  # 👉️ 100

        # 👇️ accessing parent class variable
        print(self.cls_id)  # 👉️ emp-cls


d1 = Developer('bobbyhadz')
print(d1.salary)  # 👉️ 100

print(d1.cls_id)  # 👉️ 'emp-cls'