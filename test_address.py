# -*- coding = utf-8 -*-
"""
企业微信 通讯录相关功能的测试用例，比如：添加/删除成员
@time      2020-5-24
@author    ShirleyZhu
"""
import time
import random
from test_selenium.wework.address_page import AddressPage
from test_selenium.wework.common import CommonMethod
from test_selenium.wework.ww_driver import WWDriver


class TestAddress:
    def setup(self):
        """
        初始化操作
        """
        self.w_driver = WWDriver()            # 实例化一个 webdriver
        self.address = AddressPage(self.w_driver)           # 实例化 通讯录 页面
        self.common = CommonMethod()            # 实例化公共类

    def teardown(self):
        """
        执行完用例后的操作
        """
        # todo: 查找报错原因
        # self.w_driver.quit()          # 报错：没有quit()属性
        self.w_driver.driver.quit()
        # pass

    def test_add_mem(self):
        """
        添加通讯录的成员
        """
        random_no = random.randint(5, 200)
        phone_ran = random.randint(100, 999)
        tips_no = self.address.add_member("张菲尼", random_no, "1786"+str(phone_ran)+"0973")
        # 断言添加成员是否成功
        self.common.assert_tips(tips_no)

    def test_del_mem(self):
        pass

    def test_edit_info(self):
        """
        编辑成员详情页
        """
        tips_no = self.address.search_mem("张").edit_info("李小二")
        # 断言修改信息是否成功
        self.common.assert_tips(tips_no)
