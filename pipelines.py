# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Article.modules.es_type import ArticleType
from w3lib.html import remove_tags


class ArticlePipeline(object):
    def process_item(self, item, spider):
        return item

class ElasticsearchPipeline(object):
    #将数据写入到es中
    def process_item(self, item, spider):
        #将item转换为es的数据
        article = ArticleType()
        article.title = item['title']
        article.content = remove_tags(item["content"])
        article.url = item["url"]
        article.meta.id = item["url_object_id"]
        article.save()
        return item