# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from estate.items import EstateItem


class ThepaperSpider(CrawlSpider):
    name = "thepaper"

    location = "qg"

    allowed_domains = [
        "www.thepaper.cn"
    ]
    
    start_urls = (
        'http://www.thepaper.cn/load_index.jsp?nodeids=25433&topContIds=&pageidx={}'.format(d) for d in range(1,50)
    )

    rules = (
        Rule(LinkExtractor(allow=('/newsDetail_forward_\d+')), callback='parse_post'),
    )

    def parse_post(self, response):

        # from scrapy.shell import inspect_response
        # inspect_response(response)
        date_str = response.css('.news_other span::text').extract()[0].split()[0]

        post_url = response.url

        if post_url.startswith('http://www.thepaper.cn/newsDetail_forward'):
            item = EstateItem()


            item['url'] = post_url
            item['website'] = self.name
            item['location'] = self.location
            item['published_at'] = datetime.strptime(date_str, '%Y-%m-%d')
            item['html'] = response.body_as_unicode()

            yield item
