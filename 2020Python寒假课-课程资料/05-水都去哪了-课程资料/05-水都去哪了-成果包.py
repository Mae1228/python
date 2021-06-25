'''水都去哪了-成果包
对于分类数据的对比，通常可用柱状图，我们可以通过图表轻松识别最大/最小值。
当数据X轴为连续数值（如时间）且我们比较注重观察数据变化趋势时，折线图是非常好的选择'''

#第一步：导入工具箱
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line

'''柱状图'''
#第二步：创建柱状图
bar = Bar()
#对全局进行配置
bar.set_global_opts(xaxis_opts=opts.AxisOpts(name="水的用途"),
                    yaxis_opts=opts.AxisOpts(name="水量（单位/吨）"),
                    title_opts=opts.TitleOpts(title="2019年6月用水分布"))

#第三步：添加数据
bar.add_xaxis(["饮用水", "实验用水", "打水仗", "清洁用水"])
bar.add_yaxis("阿短", [20, 50, 10, 80])
#bar.add_yaxis("编程猫", [15,10,30,1])

#第二步：创建柱状图（渲染并保存）
bar.render("2019年6月用水分布(成果包).html")

'''折线图'''
#第二步：创建折线图
line = Line()
#对全局进行配置
line.set_global_opts(xaxis_opts=opts.AxisOpts(name="月份"), 
                     yaxis_opts=opts.AxisOpts(name="水量（单位/吨）"),
                     title_opts=opts.TitleOpts(title="2019年用水情况"))

#第三步：添加数据
line.add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月","7月", "8月", "9月", "10月", "11月", "12月"])
line.add_yaxis("阿短", [6.80, 4.10, 7.00, 8.50, 5.80,4.20, 7.80, 9.40, 8.00, 4.60, 8.50, 9.80])
line.add_yaxis("编程猫", [4.80, 4.10, 6.00, 6.50, 5.80,5.20, 6.80, 7.40, 6.00, 5.60, 7.50, 7.80])

#第二步：创建折线图（渲染并保存）
line.render("2019年用水情况(成果包).html")