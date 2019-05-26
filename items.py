# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from w3lib.html import remove_tags


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    print("-------------do items------------")
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    content =scrapy.Field(
        input_processor=MapCompose(remove_tags)
    )
    print("-----------item succeed-------------")
