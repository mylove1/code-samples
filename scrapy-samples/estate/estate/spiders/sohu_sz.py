# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class SohuShSpider(CrawlSpider):
    name = "sohu_sz"

    location = "sz"

    allowed_domains = [
        "sz.focus.cn",
    ]
    
    start_urls = (
        'http://sz.focus.cn/newscenter/news-bendixinwen/p1/',
        'http://sz.focus.cn/newscenter/news-shichangdongtai/p1',
        'http://sz.focus.cn/newscenter/news-hongguanzhengce/p1',
    )

    rules = (
        Rule(LinkExtractor(allow=('/newscenter/news-bendixinwen/p\d+/',)), follow=True),
        Rule(LinkExtractor(allow=('/newscenter/news-shichangdongtai/p\d+/',)), follow=True),
        Rule(LinkExtractor(allow=('/newscenter/news-hongguanzhengce/p\d+/',)), follow=True),
        Rule(LinkExtractor(allow=('/news/\d+-\d+-\d+/\d+\.html')), callback='parse_post'),
    )

    # @todo: 需要再梳理页面抓取逻辑

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        post_url = response.url

        if post_url.startswith('http://sz.focus.cn/news/'):
            item = EstateItem()

            item['url'] = post_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(post_url.split('/')[-2], '%Y-%m-%d')
            item['html'] = response.body_as_unicode()

            yield item
