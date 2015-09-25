# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EstateItem(scrapy.Item):
    url = scrapy.Field()
    website = scrapy.Field()
    location = scrapy.Field()
    published_at = scrapy.Field()
    html = scrapy.Field()


# class SinaXmItem(scrapy.Item):
#     """ Sina Xm Item """
#     url = scrapy.Field()
#     published_at = scrapy.Field()
#     content = scrapy.Field()
