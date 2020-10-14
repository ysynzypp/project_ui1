# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 14:18
# @Author  : mao
# @Explain : 浏览器启动的基类
import time
import os
from selenium import webdriver
from common.log import logger

"""如果需要使用其他浏览器，可在dict中新增其他浏览器的webdriver"""
TYPES = {'chrome': webdriver.Chrome, }
EXECUTABLE_PATH = {'chrome': '../driver/chromedriver.exe', }


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        # else:
        #     raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None




    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    a = Browser()
    c = a.get('http://www.baidu.com')
    time.sleep(2)
    a.close()
