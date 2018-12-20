# -*- coding:utf-8 -*-
import re

SONGID = '190449'
SONGNAME = '吻别'
LIMIT_NUM = 100

PATTERN = re.compile(r'[\n\t\r\/]')	#替换掉评论中的特殊字符以防插入数据库时报错

DATABASE = '****'
TABLE_COMMENTS = '****'
TABLE_USERS = '****'
HOST = '****'
USER = '****'
PASSWD = '****'

ROOT_URL = 'http://music.163.com/api/v1/resource/comments/R_SO_4_'+SONGID+'?limit='+str(LIMIT_NUM)+'&offset=%s'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Host': 'music.163.com',
    'Cookie': '****',
}
