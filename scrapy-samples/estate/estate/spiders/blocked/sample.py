# -*- coding: utf-8 -*-
import scrapy


class SampleSpider(scrapy.Spider):
    name = "sample"
    allowed_domains = ["sample.com"]
    start_urls = (
        'http://www.sample.com/',
    )

    def parse(self, response):
        pass
