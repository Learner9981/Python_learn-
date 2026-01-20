'''
Q1. wha tis join method?
Q2. How it works?
Q3. Real time usage of join method?

'''

# names = ["Pawan","Ram", "Manish"]

# final_result =" "
# for name in names:
#     final_result+= name 
#     final_result = final_result + " "+ name
#     final_result = " ".join(names)

# lst_of_num = ['1','2','3','4','5','6']

# result = " ".join(lst_of_num)
# print(result)

state_dept_info = [{"State":"Bihar","Department":"IT"}
                    ,{"State":"Delhi","Department":"Marketing"}]

''' Find out all the employee name who are available in the above condition.
You don't know the exact number of filter condition. which will come in the above list it can change in each run .'''

query = '''select * from (
    select e.employee_name,e.state,e.zip,e.zip,e.salary,d.Department
    from employee_tbl e
    inner join department d 
    ON e.emp_id = d.emp_id
    )a
    where salary > 10000 '''
    
final_filter_condition = []

for condition in state_dept_info:
    for key,value in condition.items():
       final_filter_condition.append(f"{key} = {value}")
# print(final_filter_condition)

result = " OR ".join(final_filter_condition)
print(query + " AND " + result)
