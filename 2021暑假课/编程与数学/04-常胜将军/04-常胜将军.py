spare = 21
print("游戏开始:")
while True:
    print("---------剩余火柴数量为：", spare, "---------")
    gamer = int(input("你取火柴: "))
    if gamer < 1 or gamer > 4 or gamer > spare:
        print("你取的火柴数量犯规！")
        continue
    spare -= gamer
    if spare == 0:
        print("计算机获胜，游戏结束")
        break
    computer = 5 - gamer
    spare -= computer
    print("计算机取火柴:", computer)
    if spare == 0:
        print("你获胜，游戏结束！")
        break
