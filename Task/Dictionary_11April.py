# total marks of multiple students

# student_data={
#     "std1":{"name":"shivam","age":20,"course":"DA","marks":[45,36,28]},
#     "std2":{"name":"aditya","age":20,"course":"Ds","marks":[40,30,20]},
#     "std3":{"name":"hitesh","age":22,"course":"B.Com","marks":[65,80,96]}
# }

# grand_total=0
# for k,v in student_data.items():
#     sum=0
#     for k1,v1 in v.items():
#         if type(v1)==list:
#             for i in v1:
#                 sum+=i

#     v["total_marks"]=sum
#     grand_total+=sum
# student_data["grndtotal"]=grand_total

# for i in student_data.items():
#     print(i)




# total salary of multiple employees

emp_data={
    "emp1":{"name":"shivam","age":20,"salary":"2300","incentive":[2300,1200,3400]},
    "emp2":{"name":"aditya","age":20,"salary":"4500","incentive":[2200,2500,3200]},
    "emp3":{"name":"hitesh","age":22,"salary":"3700","incentive":[4300,1200,800]}
}

grand_total=0
for k,v in emp_data.items():
    sum=0
    for k1,v1 in v.items():
        if type(v1)==list:
            for i in v1:
                sum+=i

    v["total_salary"]=sum
    grand_total+=sum
emp_data["grndtotal"]=grand_total

for i in emp_data.items():
    print(i)