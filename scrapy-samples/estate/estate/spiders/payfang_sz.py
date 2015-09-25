# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class PayfangSzSpider(CrawlSpider):
    name = "payfang_sz"

    location = "sz"

    allowed_domains = [
        "sz.payfang.com"
    ]
    
    start_urls = (
        'http://sz.payfang.com/info/loushikuaixun/{}.html'.format(d) for d in range(1, 3)
    )

    rules = (
        Rule(LinkExtractor(allow=('/html/\d+/\d+/\d+_\d+\.html')), callback='parse_post'),
    )

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        post_url = response.url

        # 处理日期
        post_url_info = post_url.split('/')
        post_date = post_url_info[4]+post_url_info[5]

        item = EstateItem()

        item['url'] = post_url
        item['website'] = self.name
        item['location'] = self.location
        item['published_at'] = datetime.strptime(post_date, '%Y%m%d')
        item['html'] = response.body_as_unicode()

        yield item
