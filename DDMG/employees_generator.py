import random
import employees

names = []
first_names = []
last_names = []

with open("first_names.txt", "r") as f:
    first_names = f.read().splitlines()
    
# random.shuffle(first_names)

with open("last_names.txt", "r") as f:
    last_names = f.read().splitlines()
    
# random.shuffle(last_names)

# for first_name, last_name in zip(first_names, last_names):
#     names.append(first_name + " " + last_name)

amount = int(input("How many employees do you want to generate? "))

for name in range(amount):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    names.append(first_name + " " + last_name)

with open("employees.txt", "w") as f:
    f.write("INSERT INTO employees\nVALUES\n")
    for x, name in enumerate(names):
        
        empid = format(x, '04d')
        employee = employees.Employees(empid, name)
        f.write(f'("E{employee.id}", "{employee.name}", {employee.departmentid}, "{employee.department}", {employee.wage}),\n')
        
