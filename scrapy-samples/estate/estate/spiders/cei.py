# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http.request import Request
from scrapy.selector import Selector

from estate.items import EstateItem

class CeiSpider(CrawlSpider):
    name = "cei"

    location = "qg"

    # http://www.realestate.cei.gov.cn/file/index.aspx?p=1&op=tt&type1=%BD%F1%C8%D5%D2%AA%CE%C5&lk=0&key1=&k=1&b=0
    # http://www.realestate.cei.gov.cn/filea/br.aspx?id=20150109161344

    allowed_domains = [
        "www.realestate.cei.gov.cn",
    ]

    start_urls = ('http://www.realestate.cei.gov.cn/file/index.aspx?p={}&op=sc&type1=%CA%D0%B3%A1&lk=&key1=&k=1&b=1'.format(x) for x in range(1, 60))

    # start_urls = (
    #     'http://www.realestate.cei.gov.cn/filea/a/xxbr.aspx?p=1&c=',
    # )

    rules = (
        #Rule(LinkExtractor(allow=('/filea/a/xxbr\.aspx?p=\d+&c=',)), follow=True),
        Rule(LinkExtractor(allow=('/file/br\.aspx\?id=\d+', )), callback='parse_post'),
    )

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        item_url = response.url

        item_id = item_url.split('=')[1]

        item = EstateItem()

        item['url'] = item_url
        item['website'] = self.name
        item['location'] = self.location
        item['published_at'] = datetime.strptime(item_id[:8], '%Y%m%d')
        item['html'] = response.body_as_unicode()

        yield item
