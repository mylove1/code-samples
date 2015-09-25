# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from estate.items import EstateItem


class FangSpider(CrawlSpider):
    name = "fang"

    location = "qg"

    allowed_domains = [
        "news.fang.com",
    ]

    # http://www.fang.com/news/gdxw/2015-01-14/1.html ## 日期为今天

    now_date = datetime.now().strftime('%Y-%m-%d')
    start_url = 'http://www.fang.com/news/gdxw/'+now_date+'/1.html'
    start_urls = (
        start_url,
    )

    # http://www.fang.com/news/2015-01-14/14629724.htm
    rules = (
        Rule(LinkExtractor(allow=('/news/gdxw/'+now_date+'/\d+\.html',)), follow=True),
        Rule(LinkExtractor(allow=('/\d+-\d+-\d+/\d+\.htm')), callback='parse_post'),
    )

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        item_url = response.url

        if item_url.startswith('http://news.fang.com/'):
            # from scrapy.shell import inspect_response
            # inspect_response(response)

            item = EstateItem()

            item['url'] = item_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(item_url.split('/')[-2], '%Y-%m-%d')
            item['html'] = response.body_as_unicode()

            yield item