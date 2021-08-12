import random
# 猜词机会
guessTimes=14
words=['chicken','dog','cat','mouse','frog']

def pickWord():
    return random.choice(words)

# 开始游戏
def play():#控制游戏逻辑
    word=pickWord()
    print('word：',word)
    while True:
        printWordWithBlanks(word)
        guess=getGuess(word)
        global guessedLetter
        guessedLetter+=guess
        if processGuess(guess,word):
            print('答案是：',word,'you win!')
            break
        if guessTimes==0:
            print('Game Over')
            print('答案：',word)
            break

#获取用户字母
def getGuess(word):#获取玩家猜的字母
    print('剩余机会：',guessTimes)
    guess=input('请输入字母：')
    if len(guess)>1:
        return list(guess)[0]
    return guess

#已猜单词收集
guessedLetter=''

# 打印已猜单词和空位
def printWordWithBlanks(word):
    displayWord=''
    for letter in word:
        if guessedLetter.find(letter)>-1:
            displayWord=displayWord+letter
        else:
            displayWord=displayWord+'-'
    print(displayWord)

# 字母验证
def processGuess(guess,word):#胜利检测功能   判断玩家猜的字母是否属于单词中的一员，并返回布尔结果
    global guessTimes
    guessTimes-=1
    for letter in word:
        if guessedLetter.find(letter)==-1:
            return False
    return True

# 开始进入游戏
play()




