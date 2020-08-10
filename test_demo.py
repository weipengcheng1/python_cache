# coding=utf-8
import json
import time

# import requests
import os

from cache import FileCache as ca, RunTime as run, RedisCache as redis

#
# options1 = {
#     'path': 'cache'
# }
# cache = ca.Cache(options1)
# print(run.RunTime())
# print(cache.getCacheKey('name'))
# print(cache.set('userInfo', '我是一段字符串', 3600))
# print(cache.get('userInfo'))
# print(cache.delete('userInfo1'))
# print(cache.has('userInfo'))
# print(cache.pull('userInfo'))
options = {
    'host': "127.0.0.1"
}
redis = redis.RedisCache(options)
print(redis.set('test', 111,expire=2))
print(redis.get('test'))
print(redis.has('test'))
print(redis.delete('test'))
