# -*- coding: utf-8 -*-
import scrapy
from Article.items import ArticleItem
from Article.modules.hash import get_md5
from scrapy.http import Request
from urllib import parse

class JobbleSpider(scrapy.Spider):
    name = "jobble"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts']

    def parse(self, response):
        print("do parse")
        post_nodes = response.xpath('//div[@class="post floated-thumb"]/div[@class="post-thumb"]//a')
        for post_node in post_nodes:
            print(post_node)
            post_url = post_node.xpath('@href').extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

    def parse_detail(self, response):
        print("do parse_detail")
        article_item = ArticleItem()
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first("")
        content = response.xpath("//div[@class='entry']").extract()[0]
        print("-------------kaishi ------------")
        article_item["url_object_id"] = get_md5(response.url)
        article_item["title"] = title
        article_item["url"] = response.url
        article_item["content"] = content
        yield article_item
        print("parse_detail finsh")

