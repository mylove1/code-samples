# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from estate.items import EstateItem


class IfengGzSpider(CrawlSpider):
    name = "ifeng_gz"

    location = "gz"

    allowed_domains = [
        "gz.house.ifeng.com",
    ]

    urls = [
        'http://gz.house.ifeng.com/news/policy/{}',
        'http://gz.house.ifeng.com/news/market/{}',
        'http://gz.house.ifeng.com/news/society/{}',
        'http://gz.house.ifeng.com/news/survey/{}',
    ]

    start_urls = (url.format(i) for url in urls for i in range(50))

    # http://house.ifeng.com/detail/2015_01_14/50223586_0.shtml
    rules = (
        #Rule(LinkExtractor(allow=('/news/policy/\d+',)), follow=True),
        #Rule(LinkExtractor(allow=('/news/market/\d+',)), follow=True),
        #Rule(LinkExtractor(allow=('/news/society/\d+',)), follow=True),
        Rule(LinkExtractor(allow=('/detail/\d{4}_\d{2}_\d{2}/\d+_\d\.shtml')), callback='parse_post'),
    )

    def parse_post(self, response):

        item_url = response.url

        if item_url.startswith('http://gz.house.ifeng.com/detail/'):
            # from scrapy.shell import inspect_response
            # inspect_response(response)

            date_str = item_url.split('/')[-2]

            item = EstateItem()

            item['url'] = item_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(date_str, '%Y_%m_%d')
            item['html'] = response.body_as_unicode()

            yield item