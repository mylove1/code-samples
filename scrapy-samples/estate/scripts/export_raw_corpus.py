# -*- coding: utf-8 -*-

import csv

from pony.orm import db_session

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateEntity

settings = get_project_settings()
csvfile_path = '../output/estate_raw_corpus_20150116.csv'


def export_all_content():
    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')

    with open(csvfile_path, 'wb') as csvfile:
        print('open csvfile!')
        writer = csv.writer(csvfile)

        print('write table head')
        table_head = ['url', 'website', 'published_at', 'content']
        writer.writerow(table_head)
        with db_session:
            print('select items!')
            for estate in EstateEntity.select().order_by(EstateEntity.id):

                table_row = [estate.url, estate.website, estate.published_at, estate.content.encode('utf-8')]
                writer.writerow(table_row)

                print('id: ', estate.id)

def test_csvfile():
    with open(csvfile_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)

        table_head = reader.next()
        print('table_head: ', table_head)

        for table_row in reader:
            json_str = table_row[3]

            print('table_row: ', table_row)


if __name__ == '__main__':
    export_all_content()
    # test_csvfile()
