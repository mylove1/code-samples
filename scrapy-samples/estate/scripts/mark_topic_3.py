# -*- coding: utf-8 -*-

'''
第三期话题标记

1
房价上涨
所有含关键词“房价 房地产价格”的舆情信息

2
成交量回暖
所有含关键词“成交 成交量”中的任意一个词，且包含关键词“回暖 涨 上涨” 中的任意一个词的舆情信息

3
公积金与首付新政
所有包含关键词“公积金 首付” 中的任意一个词，且含关键词“首套房 二套房 贷款”中的任意一个词的舆情信息

4
营业税改革
所有包含关键词“营业税”且含关键词“免征 5年 2年 改 调”中的任意一个词的舆情信息

5
房地产与股市
所有含关键词“资金 成交 成交量” 中的任意一个词，且含有关键词“股市 股票市场 证券 金融市场”中的任意一个词的舆情信息

6
开发商资金链
所有含关键词“开发商”且含有关键词“资金链”的舆情信息

7
降息
所有含关键词“降息 利率”中的任意一词的舆情信息

8
土地市场
所有含关键词“土地市场 地价 土地价格”中的任意一个词的舆情信息+所有含关键词“土地 地块”且含有关键词“流拍 溢价”中的任意一个词的舆情信息

9
房地产信托
所有含关键词“信托”的舆情信息

10
棚户区改造
所有含关键词“棚户区”的舆情信息

11
保障性住房
所有含关键词“保障性住房 保障房”的舆情信息
'''

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
TOPIC9 = 1 << 8
TOPIC10 = 1 << 9
TOPIC11 = 1 << 10


def check_topic1(seg_freq):
    if u"房价" in seg_freq or u"房地产价格" in seg_freq:
        return True
    return False

def check_topic2(seg_freq):
    if (u"成交" in seg_freq or u"成交量" in seg_freq) and\
       (u"回暖" in seg_freq or u"涨" in seg_freq or u"上涨" in seg_freq):
        return True
    return False

def check_topic3(seg_freq):
    if (u"公积金" in seg_freq or u"首付" in seg_freq) and\
       (u"首套房" in seg_freq or u"二套房" in seg_freq or u"贷款" in seg_freq):
        return True
    return False

def check_topic4(seg_freq):
    if (u"营业税" in seg_freq) and\
       (u"免征" in seg_freq or u"5年" in seg_freq or u"2年" in seg_freq or u"改" in seg_freq or u"调" in seg_freq):
        return True
    return False

def check_topic5(seg_freq):
    if (u"资金" in seg_freq or u"成交" in seg_freq or u"成交量" in seg_freq) and\
       (u"股市" in seg_freq or u"股票市场" in seg_freq or u"证券" in seg_freq or u"金融市场" in seg_freq):
        return True
    return False

def check_topic6(seg_freq):
    if u"开发商" in seg_freq and u"资金链" in seg_freq:
        return True
    return False

def check_topic7(seg_freq):
    if u"降息" in seg_freq or u"利率" in seg_freq:
        return True
    return False

def check_topic8(seg_freq):
    if (u"土地市场" in seg_freq or u"地价" in seg_freq or u"土地价格" in seg_freq) and\
       (u"土地" in seg_freq or u"地块" in seg_freq) and\
       (u"流拍" in seg_freq or u"溢价" in seg_freq):
        return True
    return False

def check_topic9(seg_freq):
    if u"信托" in seg_freq:
        return True
    return False

def check_topic10(seg_freq):
    if u"棚户区" in seg_freq:
        return True
    return False

def check_topic11(seg_freq):
    if u"保障性住房" in seg_freq or u"保障房" in seg_freq:
        return True
    return False

def mark_topic():
    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')

    with db_session:
        print('select items!')

        estates = EstateQ2Entity.select(lambda e: e.topic == None).order_by(EstateQ2Entity.id)
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

            if check_topic9(seg_freq):
                topic = topic | TOPIC9

            if check_topic10(seg_freq):
                topic = topic | TOPIC10

            if check_topic11(seg_freq):
                topic = topic | TOPIC11


            estate.topic = topic
            commit()

            if topic != 0:
                print('!!! topic: ', topic)

            print('id: ', estate.id)


if __name__ == '__main__':
    mark_topic()