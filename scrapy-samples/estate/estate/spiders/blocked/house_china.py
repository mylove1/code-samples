# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from estate.items import EstateItem


class HouseChinaSpider(CrawlSpider):
    name = "house_china"

    location = "national"

    allowed_domains = [
        "house.china.com.cn",
    ]

    start_urls = (
        'http://house.china.com.cn/News/111_{}.htm'.format(page) for page in range(0, 50)
    )

    # http://house.china.com.cn/home/view/771911.htm
    rules = (
        #Rule(LinkExtractor(allow=('/news/\d/', )), follow=True),
        #Rule(LinkExtractor(allow=('/news/\d/p\d+', )), follow=True),
        Rule(LinkExtractor(allow=('/home/view/\d+\.htm', )), callback='parse_post'),
    )

    def parse_post(self, response):

        item_url = response.url

        if item_url.startswith('http://house.china.com.cn/home/view/'):
            # from scrapy.shell import inspect_response
            # inspect_response(response)

            pubtime_span = response.css('#pubtime_baidu')

            pubtime_str = ''
            if pubtime_span:
                pubtime_str = pubtime_span.xpath('text()').extract()[0].encode('utf-8')
            else:
                print('no date, drop!')
                return

            date_info = pubtime_str.split('：')[-1].split('/')

            item = EstateItem()

            item['url'] = item_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime(year=int(date_info[0]), month=int(date_info[1]), day=int(date_info[2]))
            item['html'] = response.body_as_unicode()

            yield item