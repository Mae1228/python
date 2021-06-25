'''智能聊天机器人-成果包'''

#智能聊天机器人
#设置智能聊天机器人的基本属性
name = '菲菲'
age = '10岁'
hobby = '聊天'
hello = '你好, 嗨, 在吗, 在吗?, 哈喽, 哈喽?'
#建立对话
message = input('对菲菲说:')
#通过if判断进行回复
if message in hello:
    print(name, '说:', '嗨!我是', name, sep='')
elif message == '你多大了呀':
    print(name, '说:', '我', age, '了', sep='')
elif message == '你喜欢做什么':
    print(name, '说:', '我喜欢', hobby, '~', sep='')
else:
    print(name, '说:', '哎呀,你说什么?', sep='')