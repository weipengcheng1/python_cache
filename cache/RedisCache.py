# -*- coding: utf-8 -*-
# @Author : xiaoLangTou
# @File : RedisCache.py
# @Project: python_cache
# @CreateTime : 2020/8/9 14:11:49

# 导入模块
import os, json, logging

# 判断redis模块是否已经安装
count = 3  # 自动下载次数
while count:
    try:
        import redis  # 引入redis

        print('导入包正常')
        break
    except:
        target = 'pip install --target=' + os.getcwd() + os.sep + 'venv' + os.sep + "lib" + os.sep + 'site-packages redis'
        os.system(target)
        count -= 1
        continue


class RedisCache:
    options = {
        'host': '127.0.0.1',  # redis连接地址
        'port': 6379,  # redis端口号
        "db": 0,  # 连接数据数量
        "password": None,  # 连接密码
        "expire": 0,  # 有效时间
        "prefix": "",  # 缓存前缀
        "decode": True  # 结果数据类型,True为字符串，False为字节
    }

    # 初始化
    def __init__(self, options=None):
        self.options = RedisCache.options if None is options else options
        # 添加参数
        self.options['host'] = options['host'] if 'host' in options else RedisCache.options['host']
        self.options['port'] = options['port'] if 'port' in options else RedisCache.options['port']
        self.options['db'] = options['db'] if 'db' in options else RedisCache.options['db']
        self.options['password'] = options['password'] if 'password' in options else RedisCache.options['password']
        self.options['expire'] = options['expire'] if 'expire' in options else RedisCache.options['expire']
        self.options['prefix'] = options['prefix'] if 'prefix' in options else RedisCache.options['prefix']
        self.options['decode'] = options['decode'] if 'decode' in options else RedisCache.options['decode']

        # 连接redis
        pool = redis.ConnectionPool(host=self.options['host'], port=self.options['port'],
                                    password=self.options['password'],
                                    decode_responses=self.options['decode'])
        self.redis = redis.Redis(connection_pool=pool)

    # 获取key名称
    def getCacheKey(self, name):
        return self.options['prefix'] + name

    # 写入缓存
    def set(self, name, value, expire=None):
        """
        :param name:    缓存名称
        :param value:   存储数据
        :param expire:  有效时间(秒)
        :return: bool
        """
        # 缓存变量名
        name = self.getCacheKey(name)
        # 系列化数据
        value = json.dumps(value)
        # 过期时间的处理
        try:
            if None is not expire:
                self.redis.setex(name=name, time=expire, value=value)
            else:
                self.redis.set(name=name, value=value)
            return True
        except Exception as e:
            print("""捕捉异常%s""" % e)
            logging.info(msg=str(e))
            return False

    # 读取缓存
    def get(self, name, default=None):
        """
        :param name:  缓存变量名
        :param default:  默认值
        :return:
        """
        # 缓存变量名
        name = self.getCacheKey(name)
        content = self.redis.get(name=name)
        if None is not content:
            return json.loads(content)
        return default

    # 判断缓存
    def has(self, name):
        """
        :param name: 缓存变量名
        :return: bool
        """
        # 缓存变量名
        name = self.getCacheKey(name)
        return True if self.redis.exists(name) else False

    # 删除缓存
    def delete(self, name):
        """
        :param name: 缓存变量名
        :return: bool
        """
        # 缓存变量名
        name = self.getCacheKey(name)
        result = self.redis.delete(name)
        return True if result > 0 else False

    # 清除缓存
    def clear(self):
        self.redis.flushdb()
        return True

    # 追加(数组)缓存数据

    def push(self, name, value):
        self.redis.append(key=self.getCacheKey(name=name), value=value)
