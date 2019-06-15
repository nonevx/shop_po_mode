"""
@File : read_txt.py
@Author: nonevx
@Contact: nonevxx@gmail.com
@Date : 2019/6/15
@Desc : 读取txt文本当做参数化数据
"""


def read_txt(filename):
    filepath = "data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()