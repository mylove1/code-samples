# -*- coding: utf-8 -*-

from pony.orm import db_session
from pony.orm import commit

from bs4 import BeautifulSoup as bs

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateEntity

settings = get_project_settings()

def remove_html_tag():
    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')

    with db_session:
        print('select items!')

        estates = EstateEntity.select(lambda e: e.status == 1)
        for estate in estates:

            print('===> process: ', estate.url)

            try:
                extract_content = bs(estate.content).text
            except:
                estate.content = '[extract_error]'
                commit()
                print('extract_error')
                continue

            if extract_content:
                estate.content = extract_content
                commit()
                print('done')
            else:
                estate.content = '[no_cleaned_text]'
                commit()
                print('no_cleaned_text')




if __name__ == '__main__':
    remove_html_tag()