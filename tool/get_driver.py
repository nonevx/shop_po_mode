"""
@File : get_driver.py
@Author: nonevx
@Contact: nonevxx@gmail.com
@Date : 2019/6/15
@Desc : 获取浏览器驱动对象
"""

# 导包
from selenium import webdriver
import page


class GetDriver:
    driver = None
    # 获取driver
    @classmethod
    def get_driver(cls):
        if not cls.driver:
            # 获取浏览器驱动对象
            cls.driver = webdriver.Chrome()
            # 最大化浏览器
            cls.driver.maximize_window()
            # 打开url
            cls.driver.get(page.url)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空
            cls.driver = None
