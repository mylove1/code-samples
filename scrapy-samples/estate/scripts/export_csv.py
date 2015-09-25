# -*- coding: utf-8 -*-

import csv

from pony.orm import db_session

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateQ2Entity

settings = get_project_settings()
csvfile_path = '/home/datartisan/works/estate_corpus_20150706.csv'


def export_csv():
    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')

    with open(csvfile_path, 'wb') as csvfile:
        print('open csvfile!')
        writer = csv.writer(csvfile)

        print('write table head')

        # url, website, location, published_at, content, seg_freq, topic
        table_head = ['url', 'website', 'location', 'published_at', 'seg_freq', 'topic']
        writer.writerow(table_head)
        with db_session:
            print('select items!')
            for estate in EstateQ2Entity.select().order_by(EstateQ2Entity.id):

                table_row = [estate.url, estate.website, estate.location, estate.published_at, estate.seg_freq, estate.topic]
                writer.writerow(table_row)
                print('id: ', estate.id)


if __name__ == '__main__':
    export_csv()