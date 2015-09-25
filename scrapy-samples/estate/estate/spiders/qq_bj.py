# -*- coding: utf-8 -*-

import json
from datetime import datetime
from random import random

from bs4 import BeautifulSoup as bs

from scrapy import Spider
from scrapy import Request

from estate.items import EstateItem


class QqBjSpider(Spider):
    name = "qq_bj"

    location = "bj"

    allowed_domains = [
        "roll.house.qq.com",
        "house.qq.com",
    ]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en',
        'Referer': 'http://roll.house.qq.com/'
    }

    url_format = 'http://roll.house.qq.com/interface/roll.php?{}&cata=&site=house&date=&page={}&mode=1&of=json'

    def start_requests(self):
        req_urls = ( self.url_format.format(random(), page) for page in xrange(20) )
        for req_url in req_urls:
            yield Request(req_url, headers = self.headers, callback=self.parse_req)

    def parse_req(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response)

        resp_content = json.loads(response.body_as_unicode())
        resp_soup = bs(resp_content['data']['article_info'])

        for a in resp_soup.find_all('a'):
            item_url = a.attrs['href']
            yield Request(item_url, callback=self.parse_item)

    def parse_item(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        item_url = response.url

        item = EstateItem()

        item['url'] = item_url
        item['website'] = self.name
        item['location'] = self.location
        item['published_at'] = datetime.strptime(item_url.split('/')[-2], '%Y%m%d')
        item['html'] = response.body_as_unicode()

        yield item
