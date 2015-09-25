# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from estate.items import EstateItem


class FangchanSpider(CrawlSpider):
    name = "fangchan"

    location = "national"

    allowed_domains = [
        "www.fangchan.com",
    ]

    start_urls = (
        'http://www.fangchan.com/news/{}/p{}'.format(cate, page) for cate in range(1, 10) for page in range(0, 30)
    )

    # http://www.fangchan.com/news/2015-01-14/5960933308887273536.html
    rules = (
        #Rule(LinkExtractor(allow=('/news/\d/', )), follow=True),
        #Rule(LinkExtractor(allow=('/news/\d/p\d+', )), follow=True),
        Rule(LinkExtractor(allow=('/news/\d/\d{4}-\d{2}-\d{2}/\d+\.html', )), callback='parse_post'),
        Rule(LinkExtractor(allow=('/news/\d{4}-\d{2}-\d{2}/\d+\.html', )), callback='parse_post'),
    )

    def parse_post(self, response):

        item_url = response.url

        if item_url.startswith('http://www.fangchan.com/news/'):
            # from scrapy.shell import inspect_response
            # inspect_response(response)

            url_info = item_url.split('/')
            date_str = url_info[-2]

            item = EstateItem()

            item['url'] = item_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(date_str, '%Y-%m-%d')
            item['html'] = response.body_as_unicode()

            yield item