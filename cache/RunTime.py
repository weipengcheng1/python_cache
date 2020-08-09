# -*- coding: utf-8 -*-
# @Author : xiaoLangTou
# @File : RunTime.py
# @Project: python
# @CreateTime : 2020/8/7 17:32:25

import os


# 生成运行目录
def RunTime(default=False):
    """
    :param default:  默认返回值
    :return: bool|str   str为runtime路径
    """
    # 工作目录
    runTime = os.path.abspath('runtime')
    try:
        if not os.path.exists(runTime):
            os.mkdir(runTime, mode=0o777)
            return runTime
        else:
            return runTime
    except:
        return default
