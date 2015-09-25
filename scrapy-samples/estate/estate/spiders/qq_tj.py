# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class QqTjSpider(CrawlSpider):
    name = "qq_tj"

    location = "tj"

    allowed_domains = [
        "tianjin.house.qq.com"
    ]
    
    start_urls = (
        'http://tianjin.house.qq.com/l/news/list2012035101222.htm',
    )

    rules = (
        Rule(LinkExtractor(allow=('/l/news/list2012035101222_\d+\.htm',)), follow=True),
        Rule(LinkExtractor(allow=('/a/\d+/\d+\.htm')), callback='parse_post'),
    )

    # @todo: 需要再梳理页面抓取逻辑

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        post_url = response.url

        if post_url.startswith('http://tianjin.house.qq.com/a/'):
            item = EstateItem()

            item['url'] = post_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(post_url.split('/')[-2], '%Y%m%d')
            item['html'] = response.body_as_unicode()

            yield item
