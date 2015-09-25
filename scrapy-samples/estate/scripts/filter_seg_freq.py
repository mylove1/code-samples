# -*- coding: utf-8 -*-

import ujson as json

from pony.orm import db_session

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateEntity

settings = get_project_settings()


def filter_seg_freq():
    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')


    with db_session:
        print('select items!')
        estates = EstateEntity.select().order_by(EstateEntity.id)
        for estate in estates:

            raw_json = estate.seg_freq
            seg_freq = json.loads(raw_json)

            # @todo:

    print('total_seg_freq: ', total_seg_freq)
    print('done')




if __name__ == '__main__':
    filter_seg_freq()
