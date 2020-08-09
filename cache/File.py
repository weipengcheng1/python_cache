# -*- coding: utf-8 -*-
# @Author : xiaoLangTou
# @File : File.py
# @Project: python
# @CreateTime : 2020/8/8 23:23:57


# 写入文件
def file_write_content(filename, data):
    """
    :param filename:    文件路径
    :param data:      写入的数据
    :return:bool    返回布尔值
    """
    try:
        with open(filename, 'w+', encoding='utf-8') as file:
            file.write(data)
            file.close()
        return True
    except:
        return False


# 读取文件
def file_get_contents(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            file.close()
        return content
    except:
        return False
