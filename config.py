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
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=3dc7a0897debf669dc9b970e408592a8,1545044714077; _ntes_nuid=3dc7a0897debf669dc9b970e408592a8; WM_TID=Ltrz4mWARKBBBUAEAFdtLo6Psj9a8Ms3; __remember_me=true; MUSIC_U=923cb008ee914455448099001e0ee00c4de3f3c92a42b35d992358325262d5b1cc14faafcf2afe09e93547f998a16efee972e14fe2041526de39c620ce8469a8; __csrf=99639f021de3abf0dd9492531e6bf896; WM_NI=Kk0F4Tt2kT%2BAfA1TCQGI1zJFvHjwTDTAPHgDMAOafQOfapPHsHWfBZ6HtlnFqV%2BKfhmoqCdy7Qe1fqJSJxVgGQl5aH5anJMf3eI%2BJMYdRv1K55I8vU2kBiDgHXQjSEVTZWY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee85cc4a878988a2d28090bc8aa7d45a868f9faebb48ed8bb798d03bb4adfca5ec2af0fea7c3b92a89b500a7b760b8eea5b5aa4ba69fffb5c25b8597ff9bc94eb698a698d750989fa0a9e6508f9f8182e55b8dbaaf91d344b1989987c152f698bc8ded4eb38ae5ace564afb1bfa4e773f58fabd2e57b8a8d8699d56d858fa4d6e444f7bfa2abd06ef1bb87ccc9479bbc9e97b441f7eb87d9f55ff2b58e8ac76d8c889f8bd24f968c96b8dc37e2a3; __utmc=94650624; JSESSIONID-WYYY=cCUcC3oQE%2FayfPOM5R99eC32rfRbkU%2BWiGv7YXbaS3dw2fH1iYGgWpf%2F4xkcnUqOsBKUYd3asIb3nhWup5J%5CbtkZpDt2tZj64M4p%2F0wn%2B2nfJUuKvX6o2nFst5jaX9IVu8jQcFRw89fRm8U%2BE%2BaP4qCJUgIxsdFNJxXXYhagE6RajKoQ%3A1545219889892; __utma=94650624.1840519937.1545044715.1545211128.1545218783.12; __utmz=94650624.1545218783.12.11.utmcsr=blog.archiew.top|utmccn=(referral)|utmcmd=referral|utmcct=/2018/12/16/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%E6%AD%8C%E6%9B%B2%E8%AF%84%E8%AE%BA%E5%8F%AF%E8%A7%86%E5%8C%96%E5%88%86%E6%9E%90/; __utmb=94650624.1.10.1545218783',
}