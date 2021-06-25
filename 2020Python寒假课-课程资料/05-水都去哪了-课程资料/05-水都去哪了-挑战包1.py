'''水都去哪了-挑战包1
添加“大黄鸡”的用水数据，重新生成柱状图和折线图'''

#第一步：导入工具箱
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line

'''柱状图'''
#第二步：创建柱状图
bar = Bar()
bar.set_global_opts(xaxis_opts=opts.AxisOpts(name="水的用途"),
                    yaxis_opts=opts.AxisOpts(name="水量（单位/吨）"),
                    title_opts=opts.TitleOpts(title="2019年6月用水分布"))

#第三步：添加数据
bar.add_xaxis(["饮用水", "实验用水", "打水仗", "清洁用水"])
bar.add_yaxis("阿短", [20, 50, 10, 80])
bar.add_yaxis("编程猫", [15, 10, 30, 1])
bar.add_yaxis('大黄鸡', [30, 20, 8, 5])

#第二步：创建柱状图（渲染并保存）
bar.render("2019年6月用水分布(挑战1).html")

'''折线图'''
#第二步：创建折线图
line = Line()
line.set_global_opts(xaxis_opts=opts.AxisOpts(name="月份"), 
                     yaxis_opts=opts.AxisOpts(name="水量（单位/吨）"), 
                     title_opts=opts.TitleOpts(title="2019年用水情况"))

#第三步：添加数据
line.add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月","7月", "8月", "9月", "10月", "11月", "12月"])
line.add_yaxis("阿短", [6.80, 4.10, 7.00, 8.50, 5.80, 4.20, 7.80, 9.40, 8.00, 4.60, 8.50, 9.80])
line.add_yaxis("编程猫", [4.80, 4.10, 6.00, 6.50, 5.80, 5.20, 6.80, 7.40, 6.00, 5.60, 7.50, 7.80])
line.add_yaxis('大黄鸡', [3.10, 5.60, 7.00, 9.00, 5.00, 2.50, 5.60, 6.30, 2.30, 4.50, 1.90, 6.20])
#第二步：创建折线图（渲染并保存）
line.render("2019年用水情况(挑战1).html")
