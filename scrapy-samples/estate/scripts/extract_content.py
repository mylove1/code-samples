# -*- coding: utf-8 -*-

import sys

from pony.orm import db_session
from pony.orm import commit

from goose import Goose
from goose.text import StopWordsChinese

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateQ2Entity

settings = get_project_settings()


def extract_content():

    if len(sys.argv) >= 3:
        start_id = int(sys.argv[1])
        end_id = int(sys.argv[2])
        print('start_id: ', start_id, '  end_id: ', end_id)
    else:
        start_id = 0
        end_id = 0
        
    

    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')

    goose = Goose({'stopwords_class': StopWordsChinese})

    with db_session:

        if start_id != 0:
            print('select items!')
            for estate in EstateQ2Entity.select(lambda e: e.content is None and e.id >= start_id and e.id < end_id):

                print('===> process: ', estate.url)

                try:
                    extract_content = goose.extract(raw_html=estate.html)
                except:
                    estate.content = '[extract_error]'
                    commit()
                    print('extract_error')
                    continue

                if extract_content.cleaned_text:
                    estate.content = extract_content.cleaned_text
                    commit()
                    print('done')
                else:
                    estate.content = '[no_cleaned_text]'
                    commit()
                    print('no_cleaned_text')

        else:                    
            print('select items!')
            for estate in EstateQ2Entity.select(lambda e: e.content is None):

                print('===> process: ', estate.url)

                try:
                    extract_content = goose.extract(raw_html=estate.html)
                except:
                    estate.content = '[extract_error]'
                    commit()
                    print('extract_error')
                    continue

                if extract_content.cleaned_text:
                    estate.content = extract_content.cleaned_text
                    commit()
                    print('done')
                else:
                    estate.content = '[no_cleaned_text]'
                    commit()
                    print('no_cleaned_text')




if __name__ == '__main__':
    extract_content()