'''
Determine the total number of unique departments within the
company.
2. List the top 5 highest-paid employees, sorted in descending order
by their monthly salary.
3. Compute and present the average monthly salary of all employees
in the company.
4. Show the number of employees in each department.
5. Provide a list of employees ranked by their salary within each
department, from highest to lowest.
6
. Calculate the total monthly payroll expense for the company.
7. Determine the highest and lowest salary in the company and
identify the corresponding employees.
8
. Remove all employees with a Junior experience level and calculate
the number of remaining employees.
'''
import json
with open("C:\\Users\\DELL\\TDI_Projects\\week4\\employees_data.json","r") as file:
    Json_load = json.load(file)
print(Json_load[0])

# for dic in Json_load:
    # print(dic)
    # for v in dic.values():
    #     v = v['department']
    #     print(v)

department = {x['department']:x for x in Json_load}.values()
print(department)
                      