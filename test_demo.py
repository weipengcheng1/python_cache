# coding=utf-8
import json
import time

# import requests
import os

from cache import FileCache as ca, RunTime as run

options = {
    'path': 'cache'
}
cache = ca.Cache()
print(run.RunTime())
print(cache.getCacheKey('name'))
print(cache.set('userInfo', '我是一段字符串', 3600))
print(cache.get('userInfo'))
print(cache.delete('userInfo1'))
print(cache.has('userInfo'))
