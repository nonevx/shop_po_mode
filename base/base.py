"""
@File : base.py
@Author: nonevx
@Contact: nonevxx@gmail.com
@Date : 2019/6/15
@Desc : 基类, 抽取一些页面的公共方法
"""

# 导包
import time
from selenium.webdriver.support.wait import WebDriverWait
import page
from tool.get_log import GetLog

# 获取日志器
log = GetLog().get_log()


class Base:
    # 初始化方法
    def __init__(self, driver):
        self.driver = driver
        log.info("获取driver对象:{}".format(self.driver))

    # 查找元素的方法
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("查找:{}元素, 查找时间最多为{}".format(loc, timeout))
        # 添加显式等待, 返回元素
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        log.info("点击: {}元素".format(loc))
        self.base_find(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        # 获取元素, 打印日志
        log.info("1) 获取元素: {}".format(loc))
        ele = self.base_find(loc)
        # 清空元素, 打印日志
        log.info("2) 清空{}元素".format(loc))
        ele.clear()
        # 输入内容, 打印日志
        log.info("3) 输入: {}".format(value))
        ele.send_keys(value)

    # 获取元素文本
    def base_get_text(self, loc):
        log.info("获取{}元素文本值".format(loc))
        return self.base_find(loc).text

    # 判断元素是否存在, 返回布尔值
    def base_is_exist(self, loc):
        # 如果存在返回True, 不存在返回False, 最多等待3秒
        try:
            log.info("判断{}元素是否存在".format(loc))
            self.base_find(loc, timeout=3, poll=0.2)
            log.info("{}元素存在".format(loc))
            return True
        except Exception as ex:
            log.info("{}元素不存在, 异常信息: {}".format(loc, ex))
            return False

    # 截图
    def base_get_screenshot(self):
        log.info("断言错误, 正在截图")
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 切换frame
    def base_switch_frame(self, frame):
        # frame: id/name/元素 => 只能使用元素
        self.driver.switch_to.frame(frame)

    # 回到默认frame
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 打开首页
    def base_click_index(self):
        # 不推荐写法
        # sleep(2)
        # self.driver.get("localhost")
        # 推荐写法
        self.base_click(page.cart_index)

    # 切换窗口方法
    def base_switch_window(self, title):
        log.info("切换title为: {}的窗口".format(title))
        self.driver.switch_to.window(self.base_get_handle(title))
        log.info("执行切换title为: {}的窗口, 完毕".format(title))

    # 根据title获取handle
    def base_get_handle(self, title):
        handles = self.driver.window_handles
        for handle in self.driver.window_handles:
            log.info("正在遍历{} => {}".format(handle, handles))
            # 切换到遍历到handle的窗口
            self.driver.switch_to.window(handle)
            log.info("切换handle为{}的窗口".format(handle))
            # 获取当前窗口title判断是否等于参数传进来的title
            if self.driver.title == title:
                log.info("条件成立, 返回handle: {}".format(self.driver.current_window_handle))
                # 条件成立, 返回当前窗口handle
                return self.driver.current_window_handle
