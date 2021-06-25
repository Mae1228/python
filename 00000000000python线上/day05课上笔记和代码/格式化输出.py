#__author:  Administrator
#date:  2016/8/22

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit(): #长的像不像数字,比如200d , '200'
    salary = int(salary)
# else:
#     #print()
#     exit("must input digit") #退出程序

msg = '''
--------- info of %s --------
Name: %s
Age : %d
Job : %s
Salary: %f
You will be retired in %s years
-------- end ----------
''' % (name,name ,age ,job ,salary, 65-age )

print(msg)