# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class QqGzSpider(CrawlSpider):
    name = "qq_gz"

    location = "gz"

    allowed_domains = [
        "gz.house.qq.com"
    ]
    
    start_urls = (
        'http://gz.house.qq.com/l/gdxw/more.htm',
    )

    rules = (
        Rule(LinkExtractor(allow=('/l/gdxw/more_\d+\.htm',)), follow=True),
        Rule(LinkExtractor(allow=('/a/\d+/\d+\.htm')), callback='parse_post'),
    )

    # @todo: 需要再梳理页面抓取逻辑

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        post_url = response.url

        if post_url.startswith('http://gz.house.qq.com/a/'):
            item = EstateItem()

            item['url'] = post_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(post_url.split('/')[-2], '%Y%m%d')
            item['html'] = response.body_as_unicode()

            yield item
