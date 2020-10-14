# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 10:12
# @Author  : mao
# @Explain : 对selenium中常用的页面操作方法进行封装
import pytest
from Base.browser import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class Method(Browser):

    # get获取浏览器地址时，默认增加51秒的隐式等待时间
    def get(self, url, maximize_window=True, implicitly_wait=1):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
        desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
        return self.driver

    # 查找元素信息，采用显式等待的方式，每0.5秒查询一次，超过20秒当做超时处理,
    # 不需要被实例化调用，为后续的操作实现元素的查找
    # locator传入格式以元组格式传入，类似('id','kw')
    def _find_element(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(locator))
        return element

    # 点击事件
    def click(self, locator):
        element = self._find_element(locator)
        element.click()

    # 输入文本内容
    def send_keys(self, locator, text):
        element = self._find_element(locator)
        element.send_keys(text)

    # 屏幕截图
    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = '../report/' + 'screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    # 清除文本信息
    def clear(self, locator):
        element = self._find_element(locator)
        element.clear()

    # 获取文本内容
    def gettext(self, locator):
        element = self._find_element(locator)
        text = element.text
        if text != '':
            return text
        if text == '':
            text = element.get_attribute('value')
            return text

    '''    
        #鼠标右击
        def context_click(self,locator):
            # 定位到要右击的元素
            right = self.find_element(locator)
            # 对定位到的元素执行鼠标右键操作
            ActionChains(self.driver).context_click(right).perform()
        #鼠标左击
        def click_and_hold(self,locator):
            # 定位到鼠标按下左键的元素
            left = self.find_element(locator)
            # 对定位到的元素执行鼠标左键按下的操作
            ActionChains(self.driver).click_and_hold(left).perform()
        '''

    # 鼠标双击
    def double_click(self, locator):
        # 定位到要双击的元素
        double = self._find_element(locator)
        # 对定位到的元素执行鼠标双击操作
        ActionChains(self.driver).double_click(double).perform()

    # 鼠标移动到什么位置
    def move_to_element(self, locator):
        # 定位到鼠标移动到上面的元素
        above = self._find_element(locator)
        # 对定位到的元素执行鼠标移动到上面的操作
        ActionChains(self.driver).move_to_element(above).perform()

    # 文本下拉选择
    def select(self, locator, text):
        # text参数是要选择的文本，即下拉菜单中的值
        Select(self._find_element(locator)).select_by_visible_text(text)

    # 序号下拉选择
    def selectindex(self, locator, index):
        # index参数即下拉菜单中的第N个值
        Select(self._find_element(locator)).deselect_by_index(index)

    # JS点击
    def jsclick(self, locator):
        element = self._find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # 上传,parameter直接传绝对路径
    def upload(self, locator, parameter):
        loc = self._find_element(locator)
        tag = loc.tag_name
        if tag == 'input':
            loc.send_keys(parameter)
        else:
            loc.click()
            time.sleep(1)
            os.system(parameter)

    # 获取Url
    def judgeurl(self):
        url = self.driver.current_url
        return url

    def back(self):
        back = self.driver.back()
        return back

    def switchtowindow(self, parameter):
        all_handles = self.driver.window_handles
        return all_handles

    # 获取页面title
    def gettitle(self):
        titles = self.driver.title
        return titles

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    from selenium import webdriver
    driver = Method()
    driver.get("http://www.baidu.com/")
    driver.send_keys(('id','kw'),"测试")
    time.sleep(2)
    driver.click(('id','kw'))
    b = driver.judgeurl()
    driver.close()

