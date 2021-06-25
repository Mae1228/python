def judge(num):
    #输入数字是个位数时
    if len(num) == 1:
        if num in ["0","1","8"]:
            return True
        else:
            return False
    #输入数字是多位数时
    temp_str = ""
    for i in num:
        if i in ["2", "3", "4", "5", "7"] :
            return False
        elif i == "6":
            temp_str += "9"
        elif i == "9":
            temp_str += "6"
        else:
            temp_str += i
    if temp_str[::-1] == num:
        return True
    else:
        return False
num = input("输入要判断的数字：")
if judge(num):
    print(num+"是镜像数字")
else:
    print(num+"不是镜像数字")

