# -*- coding:utf8 -*-
import codecs

import pandas as pd
from pyecharts import Bar,Pie,Line,Scatter,Map
import os
import numpy as np
# import jieba
# import jieba.analyse
# from wordcloud import wordcloud,ImageColorGenerator
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from datetime import datetime
import pymysql
import re
import config


pattern = re.compile(r'')
def city_group(cityCode):
    city_map = {
        '11': '北京',
        '12': '天津',
        '31': '上海',
        '50': '重庆',
        '5e': '重庆',
        '81': '香港',
        '82': '澳门',
        '13': '河北',
        '14': '山西',
        '15': '内蒙古',
        '21': '辽宁',
        '22': '吉林',
        '23': '黑龙江',
        '32': '江苏',
        '33': '浙江',
        '34': '安徽',
        '35': '福建',
        '36': '江西',
        '37': '山东',
        '41': '河南',
        '42': '湖北',
        '43': '湖南',
        '44': '广东',
        '45': '广西',
        '46': '海南',
        '51': '四川',
        '52': '贵州',
        '53': '云南',
        '54': '西藏',
        '61': '陕西',
        '62': '甘肃',
        '63': '青海',
        '64': '宁夏',
        '65': '新疆',
        '71': '台湾',
        '10': '其他',
    }
    code = str(cityCode)[:2]
    return city_map[code]


conn = pymysql.connect(host=config.HOST, user=config.USER, passwd=config.PASSWD, db=config.DATABASE, charset='utf8')
# sql_comments = 'SELECT userId FROM '+TABLE_COMENTS+' WHERE songName="%s"'%(SONGNAME)
# coments_datas = pd.read_sql(sql_comments, con=conn)
# del datas['id']
# del datas['commentId']
# del datas['content']
# del datas['likedCount']
# del datas['time']
# del datas['songId']
# del datas['songName']

if not os.path.exists(r'./output'):
    os.mkdir(r'./output')

# # 评论用户分析
# # 多表关联查询
# sql_users = 'SELECT '+config.TABLE_USERS+'.id,gender,age,city FROM '+config.TABLE_USERS+','+config.TABLE_COMMENTS+' WHERE '+config.TABLE_USERS+'.userId='+config.TABLE_COMMENTS+'.userId and '+config.TABLE_COMMENTS+'.songName="%s"'
# users_datas = pd.read_sql(sql_users%(config.SONGNAME), con=conn)
# age = users_datas[users_datas['age']>1]
# age = age.id.groupby(age['age']).count()
# bar = Bar('用户年龄分布')
# bar.use_theme('dark')
# bar.add(
#     '',
#     age.index.values,
#     age.values,
#     is_fill=True,
# )
# bar.render(r'./output/'+config.SONGNAME.replace(r'/', '-')+'用户年龄分布.html')

# gender = users_datas.id.groupby(users_datas['gender']).count()
# pie = Pie('用户性别分布图')
# pie.add(
#     '',
#     ['保密', '男', '女'],
#     gender.values,
#     is_label_show=True,
#     )
# pie.render(r'./output/'+config.SONGNAME.replace(r'/','-')+'用户性别分布.html')

# users_datas['city'] = users_datas['city'].apply(city_group)
# city = users_datas.id.groupby(users_datas['city']).count()
# map1 = Map('用户地区分布图')
# map1.add(
#     '',
#     city.index.values,
#     city.values,
#     maptype='china',
#     is_visualmap=True,
#     visual_text_color="#000",
#     is_label_show=True,
# )
# map1.render(r'./output/'+config.SONGNAME.replace(r'/', '-')+'用户地区分布.html')


# 评论时间分析
sql_comments = 'SELECT id,time FROM '+config.TABLE_COMMENTS+' WHERE songName="%s"'%(config.SONGNAME)
comments_datas = pd.read_sql(sql_comments, con=conn)
comments_datas['time1'] = comments_datas['time'].dt.dayofweek
num_date = comments_datas.id.groupby(comments_datas['time1']).count()
# # print(num_date)
line1 = Line('评论数时间(按周)分布')
line1.use_theme('dark')
line1.add(
    '',
    num_date.index.values,
    num_date.values,
    is_fill=True,
)
line1.render(r'./output/'+config.SONGNAME.replace(r'/', '-')+'评论数时间(星期)分布.html')

comments_datas['time2'] = comments_datas['time'].dt.hour
num_date = comments_datas.id.groupby(comments_datas['time2']).count()
line2 = Line('评论数时间(按小时)分布')
line2.use_theme('dark')
line2.add(
    '',
    num_date.index.values,
    num_date.values,
    is_fill=True,
)
line2.render(r'./output/'+config.SONGNAME.replace(r'/', '-')+'评论数时间(小时)分布.html')

comments_datas['time3'] = comments_datas['time'].dt.date
num_date = comments_datas.id.groupby(comments_datas['time3']).count()
line3 = Line('评论数时间(按天)分布')
line3.use_theme('dark')
line3.add(
    '',
    num_date.index.values,
    num_date.values,
    is_fill=True,
)
line3.render(r'./output/'+config.SONGNAME.replace(r'/', '-')+'评论数时间(天)分布.html')

