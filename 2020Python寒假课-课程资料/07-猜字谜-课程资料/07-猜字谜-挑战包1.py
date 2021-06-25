"""
猜字谜-挑战包1
查找有意思的字谜，将字谜库中的字谜数量增加至7个。
"""
import random
import easygui as g
import sys


def quitmsg():
    re = g.msgbox("确定退出游戏吗？", title="猜字谜")
    if re:
        sys.exit()


questions = ["一月七日,猜一个字", "一只狗四个口,猜一个字", "七十二小时,猜一个字", "王先生白小姐坐在石头上",
             "九辆车,猜一个字", "查找有意思的字谜，将字谜库中的字谜数量增加至7个。", "一人一张口，口下长支手"]
answers = ["脂", "器", "晶", "碧", "轨"]
secret = random.randint(0, 6)
question = questions[secret]
answer = answers[secret]
g.msgbox("这是一个猜字谜游戏(谜底为一个汉字)，难度等级越高对应猜测次数越少，祝你好运！", title="猜字谜")
choice = g.buttonbox("请选择游戏难度：", title="猜字谜", choices=["困难", "中等", "简单"])
if choice == "困难":
    count = 1
if choice == "中等":
    count = 3
if choice == "简单":
    count = 5
g.msgbox("你选择的难度为："+choice+"  猜测次数为："+str(count), title="猜字谜")
for i in range(count):
    guess = g.enterbox("谜面：" + question, title="猜字谜", strip=False)
    if guess != None:
        if guess == answer:
            g.msgbox("恭喜，你猜对了谜底："+answer, title="猜字谜")
            break
        else:
            if i != count-1:
                g.msgbox("很遗憾，你猜错了，你还有" + str(count-1-i) + "次机会", title="猜字谜")
    else:
        quitmsg()
else:
    g.msgbox("很遗憾，所有机会已用完！谜底是："+answer, title="猜字谜")
