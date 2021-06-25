''' python笔记'''

'''
数据类型：字符串str     数字类型：整数int    浮点float      布尔类型：True和False
算术运算符7：/ （返回浮点类型）  +    -   *    %（求余数，返回int类型）  //(向下取整，返回整数类型)   **（幂运算）
赋值运算符8：=  +=  -=  /=   *=   //=  **=    %=
逻辑运算符3：and（与）：真真为真    
            or（或）：假假为假    
            not（非）：真为假，假为真
真、假：True    False
比较运算符6：>    <    ==    >=    <=    !=
成员运算符2：in
查看数据类型：type()
input默认返回类型：str
+在两种数据类型中的用法：字符串：拼接      
                       数字类型：加号
数据类型的转换：转成int：纯数字的字符串（无小数点）   
               转成float：纯数字的字符串（有小数点）
分支结构：单分支：if。。。     
         双分支：if。。。else。。。     
         多分支：if。。。elif。。。else。。。（elif有无数个）
拼接：+：没有空格，只能在字符串之间拼接       
     ，：只能在print()中使用，可以在字符串和数字进行拼接，有空格（取消空格sep="）
缩进：一个Tab    4个空格
输入：input()        输入的内容给变量接收
变量的命名：不能以数字开头，由字母，数字，_,组成（不考虑汉字）
输出：print()
循环：while循环：计算机做重复的内容
死循环：while True:   （不知道次数的循环）
跳出循环：break    只能在循环体里面使用
跳过本次循环：continue   只能在循环体里面使用
导入随机库：import random    (写在第一行)
随机产生整数：random.randint(小,大)-----包头包尾
注释：单行注释：# (Ctrl+?)       
     多行注释：三对单引号：''''''   
              三对双引号：""""""
获取字符串的长度：len(字符串类型)
获取字符串的元素：字符串的索引[]：1、正向索引：下标从0到（长度-1）
                                2、反向索引：下标从-1到（-长度）
while循环的嵌套：先执行内循环，执行完内循环才能执行外循环
*在不同类型的使用方法：在字符串中：复制
                      在数字类型：相乘
for循环：for 变量 in 序列:      
        通常跟range方法搭配使用
range(start,stop,step):产生一组数字序列
                       1、start：默认从0开始
                       2、stop：不包括stop本身
                       3、step：步长，默认是1
循环：1、while：适用于未知循环次数的循环
      2、for：适用于已知循环次数的循环，遍历序列
遍历序列：逐个访问一组数据中的元素
序列：一组数据
海龟turtle：1、导入海龟库：import turtle as t
            2、画笔移动：t.forward(长度)-----默认方向是水平向右
            3、窗口停留：t.done()
            4、设置画笔颜色：t.pencolor(颜色的字符串)--------默认是黑色
            5、设置画笔粗细：t.pensize(数值)--------默认粗细为1
            6、画笔移动固定位置：t.goto(x,y)----------默认是(0,0)
            7、落笔：t.pendown()-------默认是落笔
            8、抬笔：t.penup()
            9、画笔旋转（正多边形的内角）：向左旋转：t.left(旋转角度)
                                          向右旋转：t.right(旋转角度)
                                          正多边形的内角=((n-2)*180)/n
            10、画笔速度：t.speed(数值)--------范围是0到10
                                               大于10或小于0.5，速度=0
                                               速度=0--------最快
                                               速度=10-------快
                                               速度=6---------正常
                                               速度=3---------慢
                                               速度=1---------最慢
            11、设置背景颜色：t.bgcolor(颜色的字符串)-----------默认是白色
            12、填充三剑客：填充颜色：t.fillcolor(颜色的字符串)-----------注意：可以填充不封闭的图形
                            开始填充：t.begin_fill()
                            结束填充：t.end_fill()
            13、一个有效的形状名字符串：t.shape(五种图形的字符串)--------circle--------圆
                                                                       turtle--------海龟
                                                                       triangle------三角形
                                                                       square--------正方形
                                                                       arrow---------箭头
            14、画笔隐藏：t.hideturtle()
            15、获取当前的x坐标：t.xcor()
            16、窗口中打印文字：t.write('内容',align='center/right/left',font=('字体名称',字体大小))
            17、设置画笔颜色和填充颜色：t.color(颜色的字符串)
            18、画圆圈：t.circle(半径,弧长)---------不写弧长默认为360
            19、画笔朝向：t.setheading(数值)---------上：90
                                                    下：-90或270
                                                    左：180
                                                    右：0
            20、定义一支新笔：t1=t.Pen()
美国标准信息交换码：
把字符返回对应的 ASCII 数值，或者 Unicode 数值：
返回值是当前整数对应的 ASCII 字符：
字符串中所有的字母都变成大写：
判断字符串中的所有字母是否全是大写：

'''

