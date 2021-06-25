'''水都去哪了-挑战包2
生成自己最近两次考试的各科成绩柱状图，分析各学科学习情况'''

#第一步：导入工具箱
from pyecharts import options as opts
from pyecharts.charts import Bar

'''柱状图'''
#第二步：创建柱状图
bar = Bar()
bar.set_global_opts(xaxis_opts=opts.AxisOpts(name="科目"),
                    yaxis_opts=opts.AxisOpts(name="成绩(百分制)"),
                    title_opts=opts.TitleOpts(title="阿短两次考试成绩"))

#第三步：添加数据
bar.add_xaxis(["语文", "数学", "英语", "科学", "音乐", "美术", "体育", "劳技"])
bar.add_yaxis("期中考试", [98, 59, 88, 76, 64, 100, 99, 95])
bar.add_yaxis("期末考试", [100, 64, 85, 78, 70, 89, 100, 98])

#第二步：创建柱状图（渲染并保存）
bar.render("阿短两次考试成绩(挑战2).html")
