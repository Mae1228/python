'''蒙提霍尔悖论-挑战包'''

import random
cat = 0
monkey = 0 
for y in range(1000):
    doors = [0, 0, 0]
    selected = []
    x = random.randint(0, 2)
    doors[x] = 1
    choice = random.randint(0,2)
    res = doors.pop(choice)
    selected.append(res)
    for i in range(2):
        if doors[i] == 0:
            move = doors.pop(i)
            selected.append(move)
            break
    #第四步：必须换
    res = doors[0]
    if res == 1:
        cat += 1
    else:
        monkey +=1
print('编程猫'+str(cat),'雷电猴'+str(monkey))
