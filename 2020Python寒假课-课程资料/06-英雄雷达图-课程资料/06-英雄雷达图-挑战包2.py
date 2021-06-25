'''
英雄雷达-成果包
继续测试两个回和，依据测试成绩在雷达图上绘制两个新的图例。
'''

# 第一步：拿出工具
from pyecharts import options as opts
from pyecharts.charts import Radar
# 第二步：创建一个雷达
r = Radar()
r.add_schema(
    # 第三步：准备固定“骨架”的容器
    schema=[
        # 第四步：创建“支架骨”
        opts.RadarIndicatorItem(name="号码记忆", min_=0, max_=15, color='black'),
        opts.RadarIndicatorItem(name="反应时间", min_=0, max_=430, color='black'),
        opts.RadarIndicatorItem(name="单词记忆", min_=0, max_=130, color='black'),
        opts.RadarIndicatorItem(name="视觉记忆", min_=0, max_=15, color='black'),
        opts.RadarIndicatorItem(name="听觉能力", min_=0, max_=20000, color='black'),
        opts.RadarIndicatorItem(name="打字速度", min_=0, max_=20, color='black')
    ]
)
# 第五步：绘制能力值覆盖图形（添加图例）
data1 = [[9, 219, 96, 6, 16710, 13]]
data1[0][1] = 430 - data1[0][1]
data1[0][4] = 30000 - data1[0][4]
r.add(series_name="第一回合", data=data1, color="red")
data2 = [[11,250,103,7,17999,15]]
data2[0][1] = 430 - data2[0][1]
data2[0][4] = 30000 - data2[0][4]
r.add(series_name="第二回合", data=data2, color="blue")
data3 = [[10,210,116,8,15773,18]]
data3[0][1] = 430 - data3[0][1]
data3[0][4] = 30000 - data3[0][4]
r.add(series_name="第三回合", data=data3, color="yellow")
# 第六步：对系列进行配置
r.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                  areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
#第七步：对全局进行配置
r.set_global_opts(title_opts=opts.TitleOpts(title="英雄雷达图"))
#第八步：生成网页图片
r.render("英雄雷达图-挑战2.html")
