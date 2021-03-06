# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class FunxunShSpider(CrawlSpider):
    name = "funxun_sh"

    location = "sh"

    allowed_domains = [
        'www.funxun.com',
        'sh.funxun.com'
    ]
    
    start_urls = (
        'http://sh.funxun.com/course/ln.asp?kw=%C9%CF%BA%A3&id=32',
    )

    rules = (
        Rule(LinkExtractor(allow=('/news/32/\d+\.html')), callback='parse_post'),
    )

    # @todo: 需要再梳理页面抓取逻辑

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        post_url = response.url

        # 处理日期
        post_datetime = response.css('div.editor > span:nth-child(3)::text').extract()[0]
        post_date = post_datetime.split(' ')[0]
        y, m, d = post_date.split('-')

        item = EstateItem()

        item['url'] = post_url
        item['website'] = self.name
        item['location'] = self.location
        item['published_at'] = datetime(int(y), int(m), int(d))
        item['html'] = response.body_as_unicode()

        yield item
