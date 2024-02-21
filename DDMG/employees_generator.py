import random
import employees
from pathlib import Path

path = Path(__file__).parents[0]
output_file = "employees.txt"

names = []
shuffled_names = []
first_names = []
last_names = []

with open(f"{path}/names.txt", "r") as f:
    names = f.read().splitlines()

for name in names:
    name_parts = name.split(" ")
    first_names.append(name_parts[0])
    last_names.append(name_parts[1])

amount = int(input("How many employees do you want to generate? "))

while amount > 10000:
    amount = int(input("Total exceeds 4 digits! Try another number: "))

for name in range(amount):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    shuffled_names.append(first_name + " " + last_name)

with open(f"{path}/{output_file}", "w+") as f:
    f.write("INSERT INTO employees\nVALUES\n")
    for x, name in enumerate(shuffled_names):

        empid = format(x, "04d")
        employee = employees.Employees(empid, name)
        f.write(
            f'("E{employee.id}", "{employee.name}", {employee.departmentid}, "{employee.department}", {employee.wage}),\n'
        )

print(
    f'Generated {len(shuffled_names)} names!\nResults stored in "{path}" under "{output_file}"'
)
