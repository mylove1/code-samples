# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class SinaBjSpider(CrawlSpider):
    name = "sina_bj"

    location = "bj"

    allowed_domains = [
        "bj.house.sina.com.cn",
        "search.house.sina.com.cn"
    ]
    
    start_urls = (
        'http://search.house.sina.com.cn/bj/news/page01/',
    )

    rules = (
        Rule(LinkExtractor(allow=('/bj/news/page\d+/',)), follow=True),
        Rule(LinkExtractor(allow=('/news/\d+-\d+-\d+/\d+\.shtml')), callback='parse_post'),
    )

    # @todo: 需要再梳理页面抓取逻辑

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        post_url = response.url

        if post_url.startswith('http://bj.house.sina.com.cn/news/'):
            item = EstateItem()

            item['url'] = post_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(post_url.split('/')[4], '%Y-%m-%d')
            item['html'] = response.body_as_unicode()

            yield item
