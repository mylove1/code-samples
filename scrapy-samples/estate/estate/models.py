# -*- coding: utf-8 -*-

from datetime import datetime
from pony.orm import *

db = Database()


class EstateEntity(db.Entity):

    _table_ = 'estate'

    id = PrimaryKey(int, size=64, unsigned=True, auto=True)

    url = Required(str)
    website = Optional(str)
    location = Optional(str)
    published_at = Optional(datetime)
    html = Optional(LongUnicode)

    content = Optional(LongUnicode)
    seg_freq = Optional(LongUnicode)
    topic = Optional(int, size=64)
    status = Optional(int, size=32, unsigned=True)

# class EstateQ1Entity(db.Entity):

#     _table_ = 'estate_q1'

#     id = PrimaryKey(int, size=64, unsigned=True, auto=True)

#     url = Required(str)
#     website = Optional(str)
#     location = Optional(str)
#     published_at = Optional(datetime)
#     html = Optional(LongUnicode)

#     content = Optional(LongUnicode)
#     seg_freq = Optional(LongUnicode)
#     topic = Optional(int, size=64)
#     status = Optional(int, size=32, unsigned=True)

class EstateQ2Entity(db.Entity):

    _table_ = 'estate_q2'

    id = PrimaryKey(int, size=64, unsigned=True, auto=True)

    url = Required(str)
    website = Optional(str)
    location = Optional(str)
    published_at = Optional(datetime)
    html = Optional(LongUnicode)

    content = Optional(LongUnicode)
    seg_freq = Optional(LongUnicode)
    topic = Optional(int, size=64)
    status = Optional(int, size=32, unsigned=True)

# class SinaXmEntity(db.Entity):
#
#     _table_ = 'sina_xm'
#
#     id = PrimaryKey(int, size=64, unsigned=True, auto=True)
#     url = Required(str)
#     published_at = Optional(datetime)
#     content = Optional(LongUnicode)
