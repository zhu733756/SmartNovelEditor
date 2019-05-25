# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from SmartNovelEditor.items import NovelcrawlerItem
from scrapy.utils.project import get_project_settings
from SmartNovelEditor.common.connection import get_dbpool

settings = get_project_settings()

class NovelcrawlerPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        return cls(get_dbpool())

    def process_item(self, item, spider):
        if isinstance(item, NovelcrawlerItem) and item.get("url",""):
            if not hasattr(spider,"sid"):
                self.dbpool.runInteraction(self.get_site_id,item,spider)
            sid=int(getattr(spider,"sid",0))
            if not sid:
                print("发生错误，sid=0")
                return item
            item["sid"]=sid
            self.dbpool.runInteraction(self.save_article, item)
        return item

    def get_site_id(self,cur,item,spider):

        sql="select id from articles_query_table where url = {}".format(item["url"])
        try:
            cur.execute(sql, value)
            res=cur.fetchone()
            setattr(spider,"sid",res[0])
        except Exception as e:
            print(e, item['title'])

    def save_article(self, cur, item):
        if not (item.get('title') and item.get('content')):
            print('url={}'.format(item.get('url')))
            if not item.get('title', '').strip():
                print('未采集到title')
            if not item.get('content', '').strip():
                print('未采集到content')
            return

        print('正在保存   {}'.format(item.get('title').strip()))
        item_keys = [
            'sid',
            'title',
            'content'
        ]

        sql_tmpl = 'insert into articles_infos ({key}) values ({value}) on DUPLICATE key update {update}'
        sql = sql_tmpl.format(key=','.join(item_keys),
                              value=','.join(['%s'] * len(item_keys)),
                              update=','.join(['{} = %s'.format(key) for key in item_keys ]))
        value = [item[key] for key in item_keys] + [item[key] for key in item_keys]
        try:
            cur.execute(sql, value)
        except Exception as e:
            print(e, item['title'])


