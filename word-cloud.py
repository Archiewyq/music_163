import jieba
import pymysql
import pandas as pd
import numpy as np
from snownlp import SnowNLP
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# plt.rcParams['font.sans-serif'] = ['msyh']
plt.rcParams['axes.unicode_minus'] = False
from pyecharts import Bar,Pie,Line
import config


def getText():
	conn = pymysql.connect(host=config.HOST, user=config.USER, passwd=config.PASSWD, db=config.DATABASE, charset='utf8mb4')
	sql = 'SELECT id,content FROM '+config.TABLE_COMMENTS+' WHERE songName="%s"'
	text = pd.read_sql(sql%(config.SONGNAME), con=conn)
	return text

def getSemi(text):
	# print(type(text['content']))
	# for i in text['content']:
	# # 	print(i)
	# 	if SnowNLP(i).sentiments<0.05:
	# 		print(SnowNLP(i).sentiments,i)
	text['content'] = text['content'].apply(lambda x:round(SnowNLP(x).sentiments, 2))
	semiscore = text.id.groupby(text['content']).count()
	bar = Bar('评论情感得分')
	bar.use_theme('dark')
	bar.add(
		'',
		y_axis = semiscore.values,
		x_axis = semiscore.index.values,
		is_fill=True,
	)
	bar.render(r'./output/'+config.SONGNAME.replace(r'/', '-')+'情感得分分析.html')

	text['content'] = text['content'].apply(lambda x:1 if x>0.5 else -1)
	semilabel = text.id.groupby(text['content']).count()
	bar = Bar('评论情感标签')
	bar.use_theme('dark')
	bar.add(
		'',
		y_axis = semilabel.values,
		x_axis = semilabel.index.values,
		is_fill=True,
	)
	bar.render(r'./output/'+config.SONGNAME.replace(r'/', '-')+'情感标签分析.html')


def getWordcloud(text):
	text = ''.join(str(s) for s in text['content'] if s)
	word_list = jieba.cut(text, cut_all=False)
	stopwords = [line.strip() for line in open(r'./StopWords.txt', 'r').readlines()]
	clean_list = [seg for seg in word_list if seg not in stopwords] #去除停用词
	clean_text = ''.join(clean_list)
	# 生成词云
	cloud = WordCloud(
	    font_path = r'C:/Windows/Fonts/msyh.ttc',
	    background_color = 'white',
	    max_words = 800,
	    max_font_size = 64
	)
	word_cloud = cloud.generate(clean_text)
	# 绘制词云
	plt.figure(figsize=(12, 12))
	plt.imshow(word_cloud)
	plt.axis('off')
	plt.show()

if __name__ == '__main__':
	text = getText()
	getSemi(text)
	getWordcloud(text)