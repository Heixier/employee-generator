# employee-generator
Employee generator for SQL database testing

## Instructions ##
Download the .zip folder

Run employees_generator.py

Find the output file stored under "employees.txt"

Paste the contents of the file into your SQL query window

**IF YOU ARE NOT ADDING ANY MANUAL ENTRIES, DELETE THE COMMA AT THE END**

Run the query


hint:

INSERT INTO departments
SELECT DISTINCT departmentno, department
FROM employees;

ALTER TABLE employees
DROP COLUMN department
