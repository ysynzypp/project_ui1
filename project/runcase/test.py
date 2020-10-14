# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 10:59
# @Author  : mao
# @Explain :
import pytest
from Base.BaseMethod import *
from selenium import webdriver
import time
import os
# import sys
# from pprint import pprint
# pprint(sys.path)

class TestCase(Method):
    def test_login(self):

        self.driver.get("http://www.baidu.com/")
        self.driver.find("By.ID","kw").send_keys("测试")
        self.driver.find("By.ID","kw").click()

if __name__ == '__main__':
    a = TestCase().test_login()