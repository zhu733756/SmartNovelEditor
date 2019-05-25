# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 10:44
# @Author  : zhu733756
# @FileName: lpush.py

import redis

conn=redis.Redis(connection_pool=redis.ConnectionPool(host="127.0.0.1",port="6379",db=1))

search_url = "https://sou.xanbhx.com/search?siteid=qula&q="

conn.sadd("biquge:start_urls", "http://google.com")
