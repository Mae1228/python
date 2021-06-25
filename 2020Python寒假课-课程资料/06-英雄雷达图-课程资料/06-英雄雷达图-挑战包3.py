'''
英雄雷达-成果包
生成编程猫和阿短的“学科雷达图”，并分析他们的学科水平。
学科分别为：语文，英语，数学，体育，美术，编程（各科满分为10分）；
编程猫的各科分数分别为：5,6,8,6,7,8；
阿短的各科分数分别为：7,7,6,7,6,6。
'''

from pyecharts import options as opts
from pyecharts.charts import Radar
r = Radar()
r.add_schema(
    schema = [
        opts.RadarIndicatorItem(name='语文', min_=0, max_=10, color='black'),
        opts.RadarIndicatorItem(name='英语', min_=0, max_=10, color='black'),
        opts.RadarIndicatorItem(name='数学', min_=0, max_=10, color='black'),
        opts.RadarIndicatorItem(name='体育', min_=0, max_=10, color='black'),
        opts.RadarIndicatorItem(name='美术', min_=0, max_=10, color='black'),
        opts.RadarIndicatorItem(name='编程', min_=0, max_=10, color='black'),
    ]
)
data_mao = [[5, 6, 8, 6, 7, 8]]
r.add(series_name = '编程猫', data = data_mao, color = 'red')
data_duan = [[7, 7, 6, 7, 6, 6]]
r.add(series_name = '阿短', data = data_duan, color = 'green')
r.set_series_opts(label_opts = opts.LabelOpts(is_show = False), areastyle_opts = opts.AreaStyleOpts(opacity = 0.5))
r.set_global_opts(title_opts = opts.TitleOpts(title ='学科成绩对比图'))
r.render('学科成绩雷达图-挑战3.html')
