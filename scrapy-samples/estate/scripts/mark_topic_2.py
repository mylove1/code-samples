# -*- coding: utf-8 -*-

import ujson as json

from pony.orm import db_session
from pony.orm import commit

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateQ2Entity

settings = get_project_settings()

TOPIC1 = 1
TOPIC2 = 1 << 1
TOPIC3 = 1 << 2
TOPIC4 = 1 << 3
TOPIC5 = 1 << 4
TOPIC6 = 1 << 5
TOPIC7 = 1 << 6
TOPIC8 = 1 << 7


def check_topic1(seg_freq):
    if u"公积金" in seg_freq and u"贷款" in seg_freq:
        return True
    return False

def check_topic2(seg_freq):
    if (u"税收" in seg_freq or u"契税" in seg_freq or u"税" in seg_freq) and\
       (u"优惠" in seg_freq or u"减免" in seg_freq or u"下调" in seg_freq or u"调整" in seg_freq):
        return True
    return False

def check_topic3(seg_freq):
    if u"资金" in seg_freq and\
       (u"股市" in seg_freq or u"股票市场" in seg_freq or u"金融市场" in seg_freq):
        return True
    return False

def check_topic4(seg_freq):
    if u"开发商" in seg_freq and u"资金链" in seg_freq:
        return True
    return False

def check_topic5(seg_freq):
    if u"降息" in seg_freq or u"利率" in seg_freq:
        return True
    return False

def check_topic6(seg_freq):
    if (u"土地市场" in seg_freq or u"地价" in seg_freq or u"土地价格" in seg_freq) or\
       (u"土地" in seg_freq and (u"流拍" in seg_freq or u"溢价" in seg_freq)):
        return True
    return False

def check_topic7(seg_freq):
    if u"城投债" in seg_freq or u"准市政债" in seg_freq or u"地方债" in seg_freq:
        return True
    return False

def check_topic8(seg_freq):
    if u"信托" in seg_freq:
        return True
    return False

def mark_topic():
    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')

    with db_session:
        print('select items!')

        estates = EstateQ1Entity.select(lambda e: e.topic == None).order_by(EstateQ1Entity.id)
        for estate in estates:

            raw_json = estate.seg_freq
            seg_freq = json.loads(raw_json)
            
            topic = 0

            if check_topic1(seg_freq):
                topic = topic | TOPIC1

            if check_topic2(seg_freq):
                topic = topic | TOPIC2

            if check_topic3(seg_freq):
                topic = topic | TOPIC3

            if check_topic4(seg_freq):
                topic = topic | TOPIC4

            if check_topic5(seg_freq):
                topic = topic | TOPIC5

            if check_topic6(seg_freq):
                topic = topic | TOPIC6

            if check_topic7(seg_freq):
                topic = topic | TOPIC7

            if check_topic8(seg_freq):
                topic = topic | TOPIC8

            estate.topic = topic
            commit()

            if topic != 0:
                print('!!! topic: ', topic)

            print('id: ', estate.id)


if __name__ == '__main__':
    mark_topic()