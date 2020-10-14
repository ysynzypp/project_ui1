# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 15:05
# @Author  : mao
# @Explain :
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome(options= option)
driver.get("http://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("测试")
driver.find_element_by_id("su").click()
print(driver.title)
driver.quit()
class TestCase:
    def __init__(self):
        pass
