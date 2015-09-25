# -*- coding: utf-8 -*-

from time import sleep

from pony.orm import *

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

JD_ITEM_COMMENTS_URL = 'http://item.jd.com/1124332.html#comment'
EVALUATION = 'bad'


DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'corpus',
    'passwd': 'corpus',
    'db': 'corpus'
}

db = Database()


class Comment(db.Entity):
    """
    SQL:

    CREATE TABLE `comment` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `uuid` varchar(36) NOT NULL,
      `content` text NOT NULL,
      `evaluation` varchar(32) NOT NULL,
      PRIMARY KEY (`id`),
      KEY `index_uuid` (`uuid`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

    """

    _table_ = 'comment'

    id = PrimaryKey(int, unsigned=True, auto=True)

    uuid = Required(str)
    content = Required(LongUnicode)
    evaluation = Required(str)




def crawl():
    """
    dirty & quick
    """

    db.bind('mysql', **DB_CONFIG)
    db.generate_mapping()
    print('connect db')

    # set UA
    DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36"
    driver = webdriver.PhantomJS()

    # test UA
    # driver.get('http://httpbin.org/headers')
    # print(driver.page_source)

    driver.get(JD_ITEM_COMMENTS_URL)
    print('open page')

    WebDriverWait(driver, 2)

    # 选择评论分类
    tab_css = 'li.ui-switchable-item[clstag="shangpin|keycount|product|chaping"]'
    if EVALUATION == 'good':
        tab_css = 'li.ui-switchable-item[clstag="shangpin|keycount|product|haoping"]'

    tab_button = driver.find_element_by_css_selector(tab_css)
    tab_button.click()
    print('select comments tab: ', EVALUATION)

    while True:

        comment_els = driver.find_elements_by_css_selector('div#comment-3 div.com-table-main > div.comments-item')
        print('select comments')

        if comment_els:
            for comment_el in comment_els:
                comment_uuid = comment_el.get_attribute('data-guid')

                try:
                    comment_content = comment_el.find_element_by_css_selector('.p-comment > .desc').text
                # except NoSuchElementException:
                #     continue
                except:
                    continue

                comment_evaluation = EVALUATION

                with db_session:
                    comment = Comment.get(uuid=comment_uuid)
                    if comment:
                        print('already have this comment')
                        continue
                    comment = Comment(
                        uuid=comment_uuid,
                        content=comment_content,
                        evaluation=comment_evaluation
                    )
                    print('insert comment: ', comment_uuid)

        try:
            next_page_button = driver.find_element_by_css_selector('div#comment-3 a.ui-pager-next')
            next_page_button.click()
        except:
            print('last page')
            break

        WebDriverWait(driver, 1)

    print('Done')




def test_db():

    db.bind('mysql', **DB_CONFIG)
    db.generate_mapping()

    with db_session:
        c = Comment(
            uuid='uuid',
            content='content',
            evaluation='evaluation',
        )




if __name__ == '__main__':
    crawl()
    #test_db()

# ipython history
"""
driver.get('http://www.douban.com')

driver.get_screenshot_as_file('shot.png')
driver.get('http://item.jd.com/1124332.html#comment')
driver.get_screenshot_as_file('shot.png')
from selenium import webdriver
des = webdriver.DesiredCapabilities.PHANTOMJS
des
pdes = webdriver.common.desired_capabilities.DesiredCapabilities.PHANTOMJS
pdes
dict(pdes)
type(pdes)
driver.get_cookies()
driver.get('http://httpbin.org/headers')
driver.page_source
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36"
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap
dcap["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36"
dcap
driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.get('http://httpbin.org/headers')
driver.page_source
driver.get('http://item.jd.com/1124332.html')
driver.get_screenshot_as_file('shot.png')
driver.get('http://item.jd.com/1124332.html#comment')
driver.get_screenshot_as_file('shot.png')
driver.find_element_by_class_name?
next_button = driver.find_element_by_class_name('ui-pager-next')
next_button.text
print next_button.text
next_button.click?
next_button.click()
driver.get_screenshot_as_file()
driver.get_screenshot_as_file('shot2.png')
next_button123 = driver.find_element_by_class_name('ui-pager-next123')
comments = driver.find_element_by_css_selector('.p-comment > .desc')
comments
comments()
comments.find_elements?
comments.find_elements()
comments = driver.find_elements_by_css_selector('.p-comment > .desc')
comments
len(comments)
type(comments)
comments.count()
comments.count
comments[0].text
printcomments[0].text
print comments[0].text
%history
comments[0]
comments[0].text
print comments[0].text
stars = driver.find_elements_by_css_selector('.grade-star')

stars[0].get_attribute('class')
$%history

haoping_button = driver.find_element_by_css_selector('li.ui-switchable-item[clstag="shangpin|keycount|product|haoping"]')
"""