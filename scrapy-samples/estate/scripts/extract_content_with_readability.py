# -*- coding: utf-8 -*-

from pony.orm import db_session
from pony.orm import commit

from readability.readability import Document

from scrapy.utils.project import get_project_settings

from estate.models import db
from estate.models import EstateQ2Entity

settings = get_project_settings()


def extract_content_with_readability():
    db.bind('mysql', **settings.get('DB'))
    db.generate_mapping()
    print('connect to db!')

    with db_session:
        print('select items!')

        estates = EstateQ2Entity.select(lambda e: e.content == '[no_cleaned_text]')
        for estate in estates:

            print('===> process: ', estate.url)

            try:
                extract_content = Document(estate.html).summary()
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
    extract_content_with_readability()