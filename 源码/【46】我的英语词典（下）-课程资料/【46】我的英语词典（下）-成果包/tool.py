'''工具包'''
from pyecharts.charts import Pie
from pyecharts import options

def load_times():
    '''
    加载times文件，返回次数字典{'abbreviation':2}
    '''
    temp_dict = {}
    with open('times.txt','r') as f:
        temp_list = f.readlines()
    if len(temp_list):
        for i in temp_list:
            file_str_list = i.split("#")
            temp_dict[file_str_list[0]] = int(file_str_list[1].replace("\n",""))
    return temp_dict

def save_times(temp_dict):
    '''
    保存times文件
    '''
    with open('times.txt','w') as f:
        for i,j in temp_dict.items():
            f.write(i+'#'+str(j)+'\n')

def make_pie(temp_dict):
    '''
    使用饼图实现单词查询可视化
    '''
    menu = ["0次",'大于0但不大于5次','大于5但不大于10次','超过10次']
    num1=num2=num3 =num4=0
    for j in temp_dict.values():
        if j==0:
            num1+=1
        elif j>0 and j<=5:
            num2+=1
        elif j>5 and j<=10:
            num3 +=1
        else:
            num4 +=1
    pie = Pie()
    pie.add("",[z for z in zip(menu,[num1,num2,num3,num4])])
    pie.set_global_opts(title_opts=options.TitleOpts(title="单词查询情况"))
    pie.set_series_opts(label_opts=options.LabelOpts(formatter='{b}:{c}'))
    pie.render("单词查询情况.html")


