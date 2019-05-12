# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from functools import lru_cache
from SmartNovelEditor.items import NovelcrawlerItem
import re

@lru_cache(maxsize=32)
def get_stopwords():
    f = open("../config/stopwords.txt", "r")
    stopwords = list(map(lambda x: x.strip("\n"), f.readlines()))
    f.close()
    return stopwords

@lru_cache(maxsize=32)
def get_common_mapping():
    return {
        "一": "1",
        "二": "2",
        "两": "2",
        "三": "3",
        "四": "4",
        "五": "5",
        "六": "6",
        "七": "7",
        "八": "8",
        "九": "9",
        "零": "0",
    }

class Biquge5200Spider(RedisSpider):
    name = 'biquge5200'
    allowed_domains = ['www.biquge5200.cc','www.qu.la','www.biquge.com.cn']
    redis_key = "biquge:start_urls"
    stopwords=get_stopwords()
    s=set()

    def parse(self, response):
        aList=response.xpath('//*[@id="list"]//dd/a')
        for a in aList:
            text="".join(a.xpath("./text()").extract())
            if text in self.stopwords:
                continue
            u="".join(a.xpath("./@href").extract())
            u=self.handles_title(u)
            if not u or u in self.s:
                continue
            self.s.add(u)
            url=response.urljoin(u)
            yield Request(url,callback=self.parse_item,meta={"title":u,"article_url":response.url})

    def parse_item(self,response):

        item=NovelcrawlerItem

        p_contents=response.xpath('//*[@id="content]/p//text()').extract() \
                   or response.xpath('//*[@id="content]//text()').extract()
        item["content"]="\n".join(i for i in map(lambda x:str.strip,p_contents) if i)
        item["title"]=response.meta["title"]
        item["article_url"]=response.meta["article_url"]
        yield item

    def handles_title(self,title):
        '''
        处理标题，将汉字转化为数字，并执行去重过滤
        :param title:
        :return:
        '''
        if not title:
            return
        rep_string= "".join(re.findall(r"第(.*?)章\s+",title))
        if not rep_string:
            return
        mapping_res = list(
            map(lambda x: get_common_mapping()[x] if x in get_common_mapping() else x, rep_string))
        n = len(mapping_res)
        if n == 1:
            if mapping_res == "十":
                return "10"
            return get_common_mapping()[mapping_res]

        s=[]

        for index,r in enumerate(mapping_res):
            if r == "十":
                if index > 0:
                    continue
                s.append("1")
            elif r == "百":
                if index !=n-1:
                    continue
                s.append("00")
            elif r == "千":
                if index !=n-1:
                    continue
                s.append("000")
            elif r == "万":
                if index !=n-1:
                    continue
                s.append("0000")
            else:
                s.append(r)
        return title.replace(rep_string,"".join(s))

    def schedule_next_requests(self):
        """Schedules a request if available"""
        # TODO: While there is capacity, schedule a batch of redis requests.
        for req in self.next_requests():
            if hasattr(self,"sid"):
                delattr(self,"sid")
            self.crawler.engine.crawl(req, spider=self)









        