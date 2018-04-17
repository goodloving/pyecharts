import pyecharts
import json

with open(r'F:/文档类/python36/案例/whether/2018-4-16.json') as f:
    weather_dirt = json.load(f)

cities, highs, lows, types = [], [], [], []
weather = ['中雨', '小雨', '扬沙', '晴', '雷阵雨', '多云', '阴', '阵雨']

def get_weather():
    for i in weather_dirt:
        if weather_dirt[i] != '无数据':
            cities.append(i)
            highs.append(int(weather_dirt[i]['high'][3:(len(weather_dirt[i]['high']) - 1)]))
            lows.append(int(weather_dirt[i]['low'][3:(len(weather_dirt[i]['low']) - 1)]))
            types.append(weather_dirt[i]['type'])

def create_Bar():
    bar = pyecharts.Bar("全国各地最高气温", "2018-4-18", title_color='red', title_pos='right', width=1400, height=700, background_color='#404a59')
    bar.add("最高气温", cities, highs, mark_point=['max', 'min', 'average'], is_label_show=True, is_datazoom_show=True, legend_pos='left')
    bar.render('Bar-High.html')

def create_Two_Bar():
    bar = pyecharts.Bar("全国各地最高最低气温", "2018-4-18", title_pos='right', title_color='blue', width=1400, height=700,background_color='white')
    bar.add("最高气温", cities, highs, mark_point=['max'], legend_text_color='red', is_datazoom_show=True)
    bar.add("最低气温", cities, lows, mark_line=['min'], legend_text_color='blue')
    bar.render('Bar-High-Low.html')

def create_EffectScatter():
    es = pyecharts.EffectScatter("最低气温动态散点图", "2018-4-16", title_pos='right', title_color='blue', width=1400, height=700, background_color='white')
    es.add("最低温度", range(0, len(cities)), lows, legend_pos='center', legend_text_color='blue', symbol_size=10, effect_period=3, effect_scale=3.5, symbol='pin',is_datazoom_show=True,is_label_show=True)
    es.render("EffectScatter-low.html")

def create_Funnel():
    fl = pyecharts.Funnel("最低气温漏斗图", "2018-40-16", title_pos='left', width=1400, height=700)
    fl.add("最低气温", cities[:15], lows[:15], is_label_show=True, label_pos='inside', label_text_color='white')
    fl.render("Funnel-low.html")

def create_Guage():
    gu = pyecharts.Gauge("仪表盘图")
    gu.add("指标", "达标", 80)
    gu.render("Guage-eg.html")

def create_Geo():
    geo = pyecharts.Geo("最高气温地理坐标系图", '2018-4-16', title_color='#fff', title_pos='center', width=1200, height=600,
                        background_color='#404a95')
    geo.add("最高气温", cities, highs, is_visualmap=True, visual_range=[0, 40], visual_text_color='#fff', symbol_size=5,
            legend_pos='right', is_geo_effect_show=True)
    geo.render("Geo-Low.html")

def create_Line():
    line = pyecharts.Line("气温变化折线图", '2018-4-16', width=1200, height=600)
    line.add("最高气温", cities, highs, mark_point=['average'], is_datazoom_show=True)
    line.add("最低气温", cities, lows, mark_line=['average'], is_smooth=True)
    line.render('Line-High-Low.html')

def create_Area():
    line = pyecharts.Line("气温变化折线图", '2018-4-16', width=1200, height=600)
    line.add("最高气温", cities, highs, mark_point=['average'], is_datazoom_show=True, is_fill=True, line_opacity=0.2, area_opacity=0.4)
    line.add("最低气温", cities, lows, mark_line=['average'], is_smooth=True, is_fill=True, area_color="#000", area_opacity=0.5)
    line.render('Area-High-Low.html')

def create_Liquid():
    lq = pyecharts.Liquid("水滴球")
    lq.add("Liquid", [0.8, 0.5, 0.2], is_liquid_outline_show=False, is_liquid_animation=True)
    lq.render("LiQuid.html")

def create_Map():
    a_city = []
    for i in cities:
        a_city.append(i + '市')
    map = pyecharts.Map("湖北最低气温", width=1200, height=600)
    map.add("最低气温", a_city, lows, maptype='湖北', is_visualmap=True, visual_text_color='#000', visual_range=[-15, 20])
    map.render("Map-low.html")

def creat_WorldMap():
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ["China", "Canada", "Brazil", "Russia", "United States"]
    map = pyecharts.Map("世界地图", width=1200, height=600)
    map.add("", attr, value, maptype="world", is_visualmap=True,
            visual_text_color='#000')
    map.render('Map-World.html')

def create_Parallel():
    parallel = pyecharts.Parallel("高低温度的平行坐标系图", '2018-4-16', width=1200, height=600)
    parallel.config(cities[:20])
    parallel.add("高低温", [highs[:20], lows[:20]], is_random=True)
    parallel.render('Parallel-High-Low.html')

def create_Pie():
    sun = 0
    cloud = 0
    lit_rain = 0
    mit_rain = 0
    sail = 0
    shadom = 0
    z_rain = 0
    th_rain = 0
    for i in types:
        if i == '晴':
            sun += 1
        elif i == '多云':
            cloud += 1
        elif i == '小雨':
            lit_rain += 1
        elif i == '中雨':
            mit_rain += 1
        elif i == '阴':
            shadom += 1
        elif i == '阵雨':
            z_rain += 1
        elif i == '雷阵雨':
            th_rain += 1
        elif i == '扬沙':
            sail += 1
    pie = pyecharts.Pie("全国天气类型比例", '2018-4-16')
    pie.add('', weather, [mit_rain, lit_rain, sail, sun, th_rain, cloud, shadom, z_rain], is_label_show=True, label_text_color=None, legend_orient='vertical', radius=[40, 50], center=[50, 50])
    pie.add('', ['中雨', '小雨', '扬沙', '晴'], [lit_rain, mit_rain, sun, sail], radius=[10, 35], center=[50, 50], rosetype='area')
    pie.render('Pie-weather.html')


if __name__ == '__main__':
    get_weather()
    #create_Bar()
    #create_Two_Bar()
    #create_EffectScatter()
    #create_Funnel()
    #create_Guage()
    #create_Geo()
    #create_Line()
    #create_Area()
    #create_Liquid()
    #create_Map()
    #creat_WorldMap()
    #create_Parallel()
    #create_Pie()
