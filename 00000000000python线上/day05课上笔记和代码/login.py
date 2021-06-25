#__author:  Administrator
#date:  2016/8/22

# for i in range(1,101):
#     if i % 2 == 1:
#         print("loop:",i)
# for i in range(100):
#     if i < 50 or i > 70:
#         print(i)


#
# for i in range(1,101,2): #2 步长
#     print("loop:",i)


_user ="alex"
_passwd = "abc123"

# for i in range(3):
#     username = input("Username:")
#     password = input("Password:")
#     if username == _user and password == _passwd :
#         print("Welcome %s login...." % _user)
#         break #跳出，中断
#     else:
#         print("Invalid username or password !")
# else:
#     print("要不要脸，臭流氓啊，小虎。")

passed_authentication = False  #假，不成立


for i in range(3):
    username = input("Username:")
    password = input("Password:")
    if username == _user and password == _passwd :
        print("Welcome %s login...." % _user)
        passed_authentication = True #，真，成立
        break #跳出，中断
    else:
        print("Invalid username or password !")
if not passed_authentication:#只有在True的情况下，条件成立
    print("要不要脸，臭流氓啊，小虎。")
