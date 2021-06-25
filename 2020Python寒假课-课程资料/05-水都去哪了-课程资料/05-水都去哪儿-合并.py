from pyecharts import options as opt
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Grid
#柱状图
bar=Bar()
bar.set_global_opts(title_opts=opt.TitleOpts(title='2021年1月份用水情况'),
                    xaxis_opts=opt.AxisOpts(name='水的用途'),
                    yaxis_opts=opt.AxisOpts(name='水量(单位/吨)'  ))
bar.add_xaxis(["饮用水", "实验用水", "打水仗", "清洁用水"])
bar.add_yaxis('阿短',[20,50,10,80])
bar.add_yaxis('编程猫',[15,10,30,1])
bar.add_yaxis('大黄鸭',[30,20,20,50])
# bar.render('2021年1月用水分布(柱状图).html')
#折线图
line=Line()
line.set_global_opts(title_opts=opt.TitleOpts(title='2020年一年的用水量',pos_top='48%'),
                    xaxis_opts=opt.AxisOpts(name='水的用途'),
                    yaxis_opts=opt.AxisOpts(name='水量(单位/吨)'),
                    legend_opts=opt.LegendOpts(pos_top='48%'))
line.add_xaxis(["1月", "2月", "3月", "4月","5月", "6月", "7月", "8月","9月", "10月", "11月", "12月",])
line.add_yaxis('张三',[6.8,4.1,7,8.5,5.8,4.2,7.8,9.4,8,4.6,8.5,9.8])
line.add_yaxis('李四',[4.8,4.1,6,6.5,5.8,5.2,6.8,7.4,6,5.6,7.5,7.8])
line.add_yaxis('牛二',[5.8,8.1,3,4.5,3.8,4.2,7.8,6.4,8,6.6,4.5,8.8])
# line.render('2020年用水分布(折线图).html')
#布局排版
grid=Grid()
grid.add(chart=bar,grid_opts=opt.GridOpts(pos_bottom="60%"))
grid.add(chart=line,grid_opts=opt.GridOpts(pos_top="60%"))
grid.render('2020年用水情况(合并).html')