"""
@File : test_login.py
@Author: nonevx
@Contact: nonevxx@gmail.com
@Date : 2019/6/15
@Desc : 登录页面用例脚本
"""

# 导包
from page.page_login import PageLogin
from tool.get_driver import GetDriver
from tool.read_txt import read_txt
from tool.get_log import GetLog
import pytest


# 获取日志器
log = GetLog.get_log()


def get_data():
    # 新建空列表
    arrs = list()
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1::]


class TestLogin:
    driver = None

    # 初始化方法
    @classmethod
    def setup_class(cls):
        # 获取driver对象
        cls.driver = GetDriver.get_driver()
        # 实例化获取PageLogin对象
        cls.login = PageLogin(cls.driver)
        # 点击登录链接
        cls.login.page_click_login_link()

    # 结束方法
    @classmethod
    def teardown_class(cls):
        # 关闭驱动对象
        GetDriver.quit_driver()

    # 登录测试方法
    @pytest.mark.parametrize(("username", "pwd", "code", "success", "expect"), get_data())
    def test_login(self, username, pwd, code, success, expect):
        # 调用登录组合业务方法
        self.login.page_login(username, pwd, code)
        # 判断是否为正向用例
        if success == "True":
            try:
                # 获取昵称
                nickname = self.login.page_get_nickname()
                log.info("昵称为: {}".format(nickname))
                # 断言昵称
                assert expect == nickname, "断言昵称"
                # 点击安全退出
                self.login.page_click_logout()
                # 点击登录链接
                self.login.page_click_login_link()
            except Exception as ex:
                log.error(ex)
        else:
            try:
                # 获取异常提示信息
                error_msg = self.login.page_click_error_info()
                log.info("错误异常提示信息: {}".format(error_msg))
                assert expect == error_msg, "断言异常信息"
            except Exception as ex:
                self.login.base_get_screenshot()
                log.error("错误原因为: {}".format(ex))
                # 抛异常
                raise
            finally:
                # 点击异常提示框按钮
                self.login.page_click_error_btn()








