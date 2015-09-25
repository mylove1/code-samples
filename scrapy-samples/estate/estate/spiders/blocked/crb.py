# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class CrbSpider(CrawlSpider):
    name = "crb"

    location = "national"

    allowed_domains = [
        "www.china-crb.cn",
    ]

    # http://www.china-crb.cn/resourcelist.jsp?$CURRPAGE$=1

    # start_urls = (
    #     'http://www.china-crb.cn/resourcelist.jsp?$CURRPAGE$=1',
    # )

    start_urls = ('http://www.china-crb.cn/resourcelist.jsp?$CURRPAGE$={}'.format(i) for i in range(1, 80))

    # http://www.china-crb.cn/resource.jsp?id=25438
    rules = (
        #Rule(LinkExtractor(allow=('/resourcelist\.jsp\?\$CURRPAGE\$=\d+',)), follow=True),
        Rule(LinkExtractor(allow=('/resource\.jsp\?id=\d+')), callback='parse_post'),
    )

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        item_url = response.url

        if item_url.startswith('http://www.china-crb.cn/resource.jsp?id='):
            # from scrapy.shell import inspect_response
            # inspect_response(response)

            try:
                date_str = response.css('div.biaoticbottom > ul > li:nth-child(1)').xpath('text()').extract()[0]
            except:
                print('===> get date_str error !!!')
                return

            item = EstateItem()

            item['url'] = item_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(date_str.encode('utf-8'), '%Y年%m月%d日')
            item['html'] = response.body_as_unicode()

            yield item