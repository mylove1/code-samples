# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from estate.items import EstateItem


class WangyiSzSpider(CrawlSpider):
    name = "163_sz"

    location = "sz"

    allowed_domains = [
        "sz.house.163.com",
    ]
    
    start_urls = (
        'http://sz.house.163.com/news/',
    )

    rules = (
        #Rule(LinkExtractor(allow=('http://sz.house.163.com/[0-9a-zA-Z]+/',)), follow=True),
        Rule(LinkExtractor(allow=('http://sz.house.163.com/special/[0-9a-zA-Z_]+/',)), follow=True),
        Rule(LinkExtractor(allow=('http://sz.house.163.com/special/[0-9a-zA-Z_]+_\d{2}/',)), follow=True),

        Rule(LinkExtractor(allow=('http://sz.house.163.com/special/000741E2/[0-9a-zA-Z]+\.html',)), follow=True),
        Rule(LinkExtractor(allow=('http://sz.house.163.com/special/000741E2/[0-9a-zA-Z]+_\d{2}\.html',)), follow=True),

        Rule(LinkExtractor(allow=('/15/(04|05|06)\d{2}/\d{2}/\w+\.html')), callback='parse_item'),
    )

    def parse_item(self, response):

        item_url = response.url

        if item_url.startswith('http://sz.house.163.com'):

            date_info = item_url.split('/')
            date_str = '20'+date_info[-4]+date_info[-3]

            item = EstateItem()

            item['url'] = item_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(date_str, '%Y%m%d')
            item['html'] = response.body_as_unicode()

            yield item
