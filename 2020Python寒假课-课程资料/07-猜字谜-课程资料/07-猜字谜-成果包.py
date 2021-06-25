"猜字谜-成果包"

# 退出游戏
import sys
def quitmsg():
    re = g.msgbox("确定退出游戏吗？", title="猜字谜")
    if re:
        sys.exit()

# 第一步：导入工具箱
import easygui as g
import random

#谜面
questions = ["一月七日,猜一个字", "一只狗四个口,猜一个字",
             "七十二小时,猜一个字", "王先生白小姐坐在石头上", "九辆车,猜一个字"]
#谜底
answers = ["脂", "器", "晶", "碧", "轨"]
# 第二部：随机选取谜题
secret = random.randint(0, 4)
question = questions[secret]
answer = answers[secret]

# 第三步：设置游戏规则（图形化用户界面）
# 创建信息框:游戏介绍
# 这是一个猜字谜游戏(谜底为一个汉字)，难度等级越高对应猜测次数越少，祝你好运！
g.msgbox("这是一个猜字谜游戏(谜底为一个汉字)，难度等级越高对应猜测次数越少，祝你好运！", title="猜字谜")

# 创建按钮箱：选择难度等级
choice = g.buttonbox("请选择游戏难度：", title="猜字谜", choices=["困难", "中等", "简单"])

# 根据难度设置猜谜次数
if choice == "困难":
    count = 1
if choice == "中等":
    count = 3
if choice == "简单":
    count = 5
    
# 创建信息框，提示玩家当前选择的难度及猜谜次数
g.msgbox("你选择的难度为："+choice+"  猜测次数为："+str(count), title="猜字谜")

# 第四步：进行猜字谜游戏
# for循环实现循环count次猜谜
for i in range(count):
    # 创建输入框：输入猜测的答案
    guess = g.enterbox("谜面：" + question, title="猜字谜", strip=False)
    # 猜测结果判断
    if guess != None:
        if guess == answer:
            g.msgbox("恭喜，你猜对了谜底："+answer, title="猜字谜")
            break
        else:
            if i != count-1:
             g.msgbox("很遗憾，你猜错了，再想一想...", title="猜字谜")
    else:
        quitmsg()
# 所有机会用完了......
else:
    g.msgbox("很遗憾，所有机会已用完！谜底是："+answer, title="猜字谜")

