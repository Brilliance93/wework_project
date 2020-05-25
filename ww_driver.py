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
            "wwrtx.vst": "4cGrrjb7Ya889T0Nnan3uop6UcksFtt8p2g26QXeqXC5Sy4CkzmYMB0HFPhY_OE2xsmBpRu0XXHhh7B4rzpxuL5W5PRwxiWudaLb7UNx4AvsxrTjnTgoHynbb5YIz28P2ZN-48jKxATtH7HtREeXKF5Cto-rkbhzCm7FsDemubvdqpZHJiyypmZxLJ9DWzBFBEsv9GnT4XprhOuoNTTYH8A3L8bsjQaUMXVS8aDK53mNq3NvjENKxvgijVU56pfy7G4kayz4NuW9gRFoHeIVeA",
            "wwrtx.d2st": "a1243272",
            "wwrtx.sid": "pwvF0hQEICdX5Fgrgn0s2_EMOFSBqM5K9S-d1YM8ISID_0fHPCZQ7aF1ILFSAeNc",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325124135323",
            "wxpay.vid": "1688854139734211",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({'name': k, 'value': v})

        # 通过cookie绕过二维码验证登陆
        self.driver.get(url)
