# -*- coding = utf-8 -*-
"""
wework通讯录相关功能的方法实现，比如：添加/删除成员
@time      2020-5-24
@author    ShirleyZhu
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from test_selenium.wework.member_details_page import MemberDetailsPage
from test_selenium.wework.ww_driver import WWDriver


class AddressPage:
    def __init__(self, wework: WWDriver):
        self.driver = wework.driver

    def add_member(self, user_name, user_id, phone, **kwargs):
        """
        添加成员
        :param user_name: 成员名
        :param user_id: 成员id
        :param phone: 成员电话
        :return: 成功提示数量
        """
        # 点击 "添加成员" 按钮
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
            )
        )
        # time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="ww_operationBar"]/a[1]').click()
        # 输入名字
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(user_name+str(time.time()))
        # 输入唯一识别id号
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(user_id)
        # 输入电话号码
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys(phone)
        # 点击确认
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        # 获取tips提示数量
        ele = len(self.driver.find_elements(By.ID, "js_tips"))
        return ele

    def del_member(self):
        pass

    def search_mem(self, key):
        """
        查找成员
        :param key: 关键字
        :return: 成员详情页
        """
        # 在搜索框输入关键字
        self.driver.find_element(By.CSS_SELECTOR, ".ww_searchInput_text").send_keys(key)
        # 跳转到成员详情页
        return MemberDetailsPage(self.driver)
