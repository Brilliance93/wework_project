# -*- coding = utf-8 -*-
"""
企业微信 driver类封装
@time      2020-5-25
@author    ShirleyZhu
"""
from selenium import webdriver


class WWDriver:
    def __init__(self):
        """
        使用cookie绕过二维码验证登陆企业微信
        :return:
        """
        # 初始化浏览器
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()

        # 打开企业微信
        url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver.get(url)
        self.driver.implicitly_wait(3)

        # 设置cookie
        cookies = {
            "wwrtx.vst": "_cTK9lI-nuzO61AdasJ1li4lWb_PpIwUx-MOBAcA9pWSxb4p0Va8A5su_NRoM3lWSET0K9-kT0GeSxUI25SozBR3-tLXeZ4PeAmwBVWakK1_0H1zKKucv5aGLHxZcfdhkD-d5IowiaavFYR3bAy9YYWPaqeM26EgUiWS2XBQjB0cJ6pCOdrFRW3JStLFxXK6ao0o_MGNzYW5cnCWK_yFjHHcQaRsMTy2MY_SU44WY4OZDUcqErWtIUivJxoOmoRHYHfN-eckShmdZ1Vo2iyHzA",
            "wwrtx.d2st": "a9807710",
            "wwrtx.sid": "pwvF0hQEICdX5Fgrgn0s21U35pUi7zSulQvyjAdz-CCE1evjoOQNLHzKBcoojg88",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325124135323",
            "wxpay.vid": "1688854139734211",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({'name': k, 'value': v})

        # 通过cookie绕过二维码验证登陆
        self.driver.get(url)
