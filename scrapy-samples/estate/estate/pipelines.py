# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pony.orm import db_session

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateEntity

settings = get_project_settings()


class EstatePipeline(object):

    def __init__(self):
        db.bind('mysql', **settings.get('DB'))
        db.generate_mapping()

    def process_item(self, item, spider):

        item_url = item['url']

        with db_session:
            estateEntity = EstateEntity.get(url = item_url)

            if estateEntity:
                print('already have this url item')
                return

            estateEntity = EstateEntity(
                url = item_url,
                published_at = item['published_at'],
                website = item['website'],
                location = item['location'],
                html = item['html']
            )

            print('url: ', item_url)
            print('save post')

    def spider_closed(self, spider):
        db.disconnect()


# class SinaXmPipeline(object):
#
#     def __init__(self):
#         db.bind('mysql', **settings.get('DB'))
#         db.generate_mapping()
#
#     def process_item(self, item, spider):
#
#         post_url = item['url']
#
#         with db_session:
#             sinaXmEntity = SinaXmEntity.get(url = post_url)
#
#             if sinaXmEntity:
#                 print('already have this url post')
#                 return
#
#             sinaXmEntity = SinaXmEntity(
#                 url = post_url,
#                 published_at = item['published_at'],
#                 content = item['content']
#             )
#
#             print('url: ', post_url)
#             print('save post')
#
#     def spider_closed(self, spider):
#         db.disconnect()