# -*- coding: utf-8 -*-

import os
import re
from collections import Counter

import jieba
import ujson as json

from pony.orm import db_session
from pony.orm import commit

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateQ2Entity

settings = get_project_settings()
accepted_token_patten = re.compile(ur"[\u4E00-\u9FA5]{2,}")

cur_path = os.path.dirname(os.path.abspath(__file__))

stop_words_file_path = os.path.join(cur_path, 'stop_words.txt')

userdict_file_path = os.path.join(cur_path, 'userdict.txt')
jieba.load_userdict(userdict_file_path)


def load_stop_words():
    stop_words = []
    with open(stop_words_file_path, 'r') as f:
        lines = f.readlines()
        stop_words = [line.decode('utf-8').strip() for line in lines]
    return stop_words

stop_words = load_stop_words()


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def token_condition(t):
    if not accepted_token_patten.match(t):
        return False

    if t in stop_words:
        return False

    return True


def segment(raw_text):

    tokens = jieba.tokenize(raw_text)
    seg_list = [w for (w, start_pos, stop_pos) in tokens if token_condition(w)]

    seg_freq_counter = Counter(seg_list)
    seg_freq = dict(seg_freq_counter)

    return json.dumps(seg_freq)


def items_segment():
    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')

    with db_session:
        print('select items!')

        estates = EstateQ2Entity.select(lambda e: e.content != None).order_by(EstateQ2Entity.id)
        for estate in estates:

            if estate.content:
                try:
                    seg_freq_res = segment(estate.content)
                except:
                    estate.status = 2
                    commit()
                    continue

                estate.seg_freq = seg_freq_res
                commit()
                print('==> id: ', estate.id)


if __name__ == '__main__':
    items_segment()