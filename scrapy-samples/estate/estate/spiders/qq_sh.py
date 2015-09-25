# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class QqShSpider(CrawlSpider):
    name = "qq_sh"

    location = "sh"

    allowed_domains = [
        "sh.house.qq.com"
    ]
    
    start_urls = (
        'http://sh.house.qq.com/l/shloushi/list.htm',
    )

    rules = (
        Rule(LinkExtractor(allow=('/l/shloushi/list_\d+\.htm',)), follow=True),
        Rule(LinkExtractor(allow=('/a/\d+/\d+\.htm')), callback='parse_post'),
    )

    # @todo: 需要再梳理页面抓取逻辑

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        post_url = response.url

        if post_url.startswith('http://sh.house.qq.com/a/'):
            item = EstateItem()

            item['url'] = post_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(post_url.split('/')[-2], '%Y%m%d')
            item['html'] = response.body_as_unicode()

            yield item
