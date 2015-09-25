# -*- coding: utf-8 -*-

import urllib2
import random


def main():
    req_url = 'http://roll.house.qq.com/interface/roll.php?0.960287460591644&cata=&site=house&date=&page=2&mode=1&of=json'
    
    request = urllib2.Request(req_url, headers={"Referer" : "http://roll.house.qq.com/"})
    contents = urllib2.urlopen(request).read()


if __name__ == '__main__':
    main()
