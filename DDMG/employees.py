import random

departments = {1: "IT",
               2: "Finance",
               3: "HR",
               4: "Sales",
               5: "Marketing"
}

class Employees():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.departmentid = random.choice(list(departments.keys()))
        self.department = departments[self.departmentid]
        self.wage = random.randrange(30, 200, 10)