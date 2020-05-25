# -*- coding = utf-8 -*-
"""
成员详情页信息
@time      2020-5-24
@author    ShirleyZhu
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MemberDetailsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def edit_info(self, rename):
        """
        编辑成员详情页信息
        :param rename: 成员名
        :return: tips 提示数量
        """
        self.driver.find_element(By.CSS_SELECTOR, ".js_edit").click()
        username = self.driver.find_element(By.NAME, "username")
        username.clear()
        username.send_keys(rename+str(time.time()))
        self.driver.find_element(By.CSS_SELECTOR, ".js_save").click()
        ele = len(self.driver.find_elements(By.ID, "js_tips"))
        return ele

    def disable_member(self):
        pass

    def del_member(self):
        pass
