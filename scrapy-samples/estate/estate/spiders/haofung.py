# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class HaofungSpider(CrawlSpider):
    name = "haofung"

    location = "qg"

    allowed_domains = [
        "www.haofung.com"
    ]
    
    start_urls = (
        'http://www.haofung.com/news/list-78-{}.html'.format(d) for d in range(1, 51)
    )

    rules = (
        Rule(LinkExtractor(allow=('/news/show-\d+\.html')), callback='parse_post'),
    )

    # @todo: 需要再梳理页面抓取逻辑

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        post_url = response.url

        # 处理日期
        post_date = response.css('div.titBar > p > span:nth-child(1)::text').extract()[0]

        item = EstateItem()

        item['url'] = post_url
        item['website'] = self.name
        item['location'] = self.location
        item['published_at'] = datetime.strptime(post_date, '%Y-%m-%d')
        item['html'] = response.body_as_unicode()

        yield item
