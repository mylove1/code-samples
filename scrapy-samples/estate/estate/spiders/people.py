# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from estate.items import EstateItem


def date_generator(days):
    now_date = datetime.now()
    for d in range(0, days+1):
        delta = timedelta(days=d)
        res_date = now_date - delta
        yield res_date.strftime('%Y%m%d')

class PeopleSpider(CrawlSpider):
    name = "people"

    location = "qg"

    allowed_domains = [
        "house.people.com.cn",
    ]

    # http://house.people.com.cn/GB/194441/review/20150114.html # 按日期查询

    start_urls = (
        'http://house.people.com.cn/GB/194441/review/{}.html'.format(d) for d in date_generator(99)
    )

    # http://www.fang.com/news/2015-01-14/14629724.htm
    rules = (
        #Rule(LinkExtractor(allow=('/news/gdxw/'+now_date+'/\d+\.html',)), follow=True),
        Rule(LinkExtractor(allow=('/n/\d{4}/\d{4}/c\d+-\d+\.html')), callback='parse_post'),
    )

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        item_url = response.url

        if item_url.startswith('http://house.people.com.cn/n/'):
            # from scrapy.shell import inspect_response
            # inspect_response(response)

            date_info = item_url.split('/')
            date_str = date_info[-3]+date_info[-2]

            item = EstateItem()

            item['url'] = item_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(date_str, '%Y%m%d')
            item['html'] = response.body_as_unicode()

            yield item