# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class FunxunTjSpider(CrawlSpider):
    name = "funxun_tj"

    location = "tj"

    allowed_domains = [
        'www.funxun.com',
        'tj.funxun.com'
    ]
    
    start_urls = (
        'http://tj.funxun.com/course/Articlelist.asp?kw=&id=32&page={}&pcount=2052&tt=%BD%F1%C8%D5%CD%B7%CC%F5'.format(d) for d in range(1,60)
    )

    rules = (
        Rule(LinkExtractor(allow=('/news/32/\d+\.html')), callback='parse_post'),
    )

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
