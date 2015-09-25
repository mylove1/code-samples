# -*- coding: utf-8 -*-

import ujson as json
from collections import Counter

from pony.orm import db_session

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateEntity

settings = get_project_settings()


def merge_seg_freq():
    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')

    total_seg_freq = Counter()

    with db_session:
        print('select items!')
        estates = EstateEntity.select().order_by(EstateEntity.id)
        for estate in estates:

            raw_json = estate.seg_freq
            seg_freq = json.loads(raw_json)
            total_seg_freq.update(seg_freq)

            print('id: ', estate.id)

    print('total_seg_freq: ', total_seg_freq)
    print('done')




if __name__ == '__main__':
    merge_seg_freq()
