# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.PhantomJS()
driver.get('http://ditu.amap.com/search?query=%E6%8E%92%E6%A1%A3&city=350200&pagenum=2')

WebDriverWait(driver, 3)

items = driver.find_elements_by_css_selector('.poibox.poibox-normal.amap-marker')

print(items[0].text)

