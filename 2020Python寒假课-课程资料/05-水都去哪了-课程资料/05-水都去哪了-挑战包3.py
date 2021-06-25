'''水都去哪了-挑战包3
生成家庭内两年内的电费支出折线图，分析用电情况'''

#第一步：导入工具箱
from pyecharts import options as opts
from pyecharts.charts import Line

'''折线图'''
#第二步：创建折线图
line = Line()
line.set_global_opts(xaxis_opts=opts.AxisOpts(name="月份"), 
                     yaxis_opts=opts.AxisOpts(name="电费（单位/元）"), 
                     title_opts=opts.TitleOpts(title="2018-2019年缴电费情况"))

#第三步：添加数据
line.add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月","7月", "8月", "9月", "10月", "11月", "12月"])
line.add_yaxis("2018", [19.81, 18.12, 17.22, 18.23, 25.43,33.90, 34.54, 32.40, 18.00, 15.63, 18.50, 19.80])
line.add_yaxis("2019", [22.81, 19.12, 17.52, 19.23, 23.43,32.90, 35.54, 34.40, 10.30, 17.63, 20.59, 18.81])

#第二步：创建折线图（渲染并保存）
line.render("2018-2019年缴电费情况(挑战3).html")
