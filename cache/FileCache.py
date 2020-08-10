# -*- coding: utf-8 -*-
# @Author : xiaoLangTou
# @File : FileCache.py
# @Project: python
# @CreateTime : 2020/8/6 23:13:35

import os, json, time, hashlib, zlib, shutil
from .RunTime import RunTime
from .File import file_get_contents, file_write_content


class Cache:
    options = {
        'expire': 0,
        "cache_subdir": True,
        'prefix': '',
        'path': '',
        'hash_type': 'md5',
        'data_compress': False
    }

    # 初始化
    def __init__(self, options=None):
        """
        :param options['expire']:   过期时间
        :param options['prefix']:   前缀
        :param options['path']:     路径
        :param options['hash_type']:  加密方式
        """
        # 当options为空时设置为dict
        # if options is None:
        #     options = {}
        # print(options)
        # 判断options是否不为空并且为dict类型
        if (options is not None) and (isinstance(options, dict)):
            self.options = options
        else:
            self.options = Cache.options
        # 判断缓存文件路径
        if ('path' in self.options) and self.options['path'] != '':
            self.options['path'] = os.path.abspath(self.options['path']) + os.sep
        else:
            self.options['path'] = os.path.abspath(RunTime() + os.sep + 'cache') + os.sep

        self.options['cache_subdir'] = options['cache_subdir'] if 'cache_subdir' in options \
            else Cache.options['cache_subdir']
        self.options['hash_type'] = options['hash_type'] if 'hash_type' in options \
            else Cache.options['hash_type']
        self.options['data_compress'] = options['data_compress'] if 'data_compress' in options \
            else Cache.options['data_compress']
        self.options['expire'] = options['expire'] if 'expire' in options \
            else Cache.options['expire']
        self.options['prefix'] = options['prefix'] if 'prefix' in options \
            else Cache.options['prefix']
        print(self.options)

    # 生成缓存文件名与路径
    def getCacheKey(self, name):
        """
        :param name: 缓存变量名
        :return:  缓存路径
        """
        # 生成hash文件名
        name = hashlib.new(self.options['hash_type'], bytes(
            name, encoding='utf-8')).hexdigest()
        #  判断是否启用子目录
        if self.options['cache_subdir']:
            name = name[0:2] + os.sep + name[2:]

        if self.options['prefix']:
            name = self.options['prefix'] + os.sep + name
        return self.options['path'] + name + ".py"

    # 写入缓存
    def set(self, name, value, expire=None):
        """
        :param name:  缓存名称
        :param value:  缓存值
        :param expire: 过期时间
        :return:bool   返回布尔值
        """
        # 有效期
        if expire is None:
            expire = self.options['expire']
        #     获取缓存文件路径
        filename = self.getCacheKey(name)
        # 获取文件名
        dir = os.path.dirname(filename)
        # 创建文件
        if not os.path.isdir(dir):
            print(dir)
            try:
                os.makedirs(dir, 0o777)
            except:
                pass
        # 将值进行序列化
        data = json.dumps(value)
        # 写内容
        data = "#%012d" % expire + "\n" + data

        res = file_write_content(filename, data)
        return True if res else False

    # 读取缓存
    def get(self, name, default=None):
        content = self.getRaw(name=name)
        return default if None is content else json.loads(content['content'])

    # 判断文件是否存在后删除
    def __unlink(self, filename):
        """
        :param filename:  文件
        :return: bool
        """
        try:
            os.path.isfile(filename) and os.remove(filename)
            return True
        except:
            return False

    # 获取缓存
    def getRaw(self, name):
        """
        :param name: 缓存名称
        :return: dict  返回缓存内容 content为内容，expire为有效时间(s)
        """
        # 获取文件名
        filename = self.getCacheKey(name=name)
        # 判断是否为文件
        if not os.path.isfile(filename):
            return
        # 读取内容
        content = file_get_contents(filename)
        # 判断文件
        if False is not content:
            # 获取有效期
            expire = int(content[9:13])
            # 判断缓存是否已经过期
            if expire != 0 and time.time() - expire > os.stat(filename).st_mtime:
                # 缓存过期删除缓存文件
                self.__unlink(filename)
                return
            content = content[14:]
            if self.options['data_compress'] is not False:
                content = zlib.compress(content)
            return {'content': content, 'expire': expire}

    # 清空缓存
    def clear(self):
        dirname = self.options['path'] + self.options['prefix']
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
            return True
        return False

    # 删除缓存
    def delete(self, name):
        """
        :param name: 缓存名称
        :return: bool
        """
        return self.__unlink(self.getCacheKey(name=name))

    # 判断缓存是否存在
    def has(self, name):
        return True if self.getRaw(name=name) is not None else False

    # 获取并删除缓存
    def pull(self, name):
        result = self.get(name=name)
        if result:
            self.delete(name=name)
            return result
