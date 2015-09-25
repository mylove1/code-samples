# -*- coding: utf-8 -*-

import urllib2

from goose import Goose
from goose.text import StopWordsChinese

url = 'http://fj.house.163.com/15/0114/08/AFTGIQ89027304UE.html'
req = urllib2.urlopen(url)
raw_html = req.read()

g = Goose({'stopwords_class': StopWordsChinese})
content = g.extract(raw_html=raw_html)

print(content)
print(content.cleaned_text[:150])