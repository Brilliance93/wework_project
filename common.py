# -*- coding=utf-8 -*-
"""
实现公共方法的封装
@time       2020-05-25
@author     ShirleyZhu
"""


class CommonMethod:

    @staticmethod
    def assert_tips(tips_no):
        """
        断言是否出现tips，出现则打印 "ok"，否则打印 "失败"
        :param tips_no: tips的个数
        :return: None
        """
        try:
            assert tips_no != 0, "失败！"
            print("OK")
        except AssertionError as error:
            print(error)
