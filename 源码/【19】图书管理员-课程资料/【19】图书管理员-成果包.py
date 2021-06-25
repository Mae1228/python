'''图书管理员-成果包'''
'''阿短一共收到了同学拿来分享的7本图书，分别是《哈利波特》、
《流浪地球》、《封神演义》、《三国演义》、《红楼梦》、《西游记》、
《水浒传》，请你基于这7本书籍建立一个书单，并实现书单展示、借书、还书的功能，
完成图书管理程序。'''

# 创建书单
lib = ['哈利波特', '流浪地球', '封神演义', '三国演义', '红楼梦', '西游记', '水浒传']
while True:
    print('end:结束管理图书', '0：展示书单', '1：借书', '2：还书')
    message = input('你好！要图书助手帮你做什么:')
    if message == 'end':  # 结束管理图书
        break
    elif message == '0':  # 展示书单
        print('目前有图书:')
        for x in lib:
            if '#' not in x:
                print(x)
            else:
                continue
    elif message == '1':  # 借书
        book = input('要借哪本书:')
        if book in lib:
            print('好的，马上帮您办理借书！')
            user = input('请登记借书人姓名:')
            bo = book + '#' + user
            lib.append(bo)
            lib.remove(book)
            print('借书成功！')
        else:
            print('没有此书或此书已被借走！')
    elif message == '2':  # 还书
        book = input('要还哪本书:')
        user = input('请核对借书人:')
        bo = book + '#' + user
        if bo in lib:
            lib.append(book)
            lib.remove(bo)
            print('还书成功！')
        else:
            print('请检查书名或借书人信息是否正确！')
