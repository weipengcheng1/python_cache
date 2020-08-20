# python_cache
基于thinkphp的文件缓存来实现的一种文件缓存，自己来练练手，慢慢的去完善

##文件缓存的使用
### 导入包
```python
from  cache import RunTime,FileCache
```
其中runtime为运行缓存目录，FileCache为文件缓存
### 配置
```python
options = {
        'expire': 0,
        "cache_subdir": True,
        'prefix': '',
        'path': '',
        'hash_type': 'md5',
        'data_compress': False
    }
```
##### options选项配置说明

| 字段 | 说明 | 数据类型 |默认值 |
| ----  |----  |----|----|
| options['expire']  | 缓存有效时间 |Number| 0(永久缓存)
| options['cache_subdir'] |  是否开启缓存子目录| Bool | True
| options['prefix']  | 缓存前缀 |str|''
| options['path']  | 缓存路径 |str|''
| options['hash_type']  | 缓存文件hash方式|str| md5
| options['data_compress']  | 缓存数据是否压缩 |bool| False

### 方法
#### 初始化化
```python
cache = cache.Cache([options])
```
其中options是可选自定义配置的，
#### 设置缓存
````python
cache.set(cacheName, cacheValue, expire)
````
````markdown
其中参数说明

cacheName      为缓存的名称

cacheValue     为缓存的值

expire         可选，缓存的有效期`
````
#### 获取缓存
```python
cache.get(cacheName,default)
```
````markdown
其中参数说明

cacheName      为缓存的名称
default        可选，可以设置默认值，默认为None
````
#### 删除缓存
```python
cache.delete(cacheName)
```
````markdown
其中参数说明
cacheName      为缓存的名称
````
#### 清空缓存
```python
cache.clear()
```
#### 先删除缓存在删除缓存
```python
cache.pull(cacheName)
```
````markdown
其中参数说明
cacheName      为缓存的名称
````

#### 判断缓存是否存在
```python
cache.has(cacheName)
```
```markdown
其中参数说明
cacheName      为缓存的名称
```
## redis缓存的使用
### 导入包
```python
from  cache import  RedisCache as redis
```
### 配置
```python
options = {
        'host': '127.0.0.1',  # redis连接地址
        'port': 6379,  # redis端口号
        "db": 0,  # 连接数据数量
        "password": None,  # 连接密码
        "expire": 0,  # 有效时间
        "prefix": "",  # 缓存前缀
        "decode": True  # 结果数据类型,True为字符串，False为字节
    }
```
##### options选项配置说明

| 字段 | 说明 | 数据类型 |默认值 |
| ----  |----  |----|----|
| options['host']  | redis连接地址 |Str| 127.0.0.1
| options['port'] |  redis端口号| Number | 6379
| options['db']  | 连接数据数量 |Number|0
| options['password']  | 连接密码 |str|None
| options['expire']  | 有效时间|Number| 0(秒)
| options['prefix']  | 缓存前缀 |str| ''
| options['decode']  | 结果数据类型 |Bool| True

### 方法
#### 初始化
```python
redis = redis.RedisCache([options])
```
其中参数说明
```markdown
options      初始化配置项，可选
```

#### 设置缓存
```python
redis.set(key, value,[expire])  #返回值：bool
```
其中参数说明
```markdown
key      缓存键名
value    缓存值
expire   缓存有效时间，可选
```
#### 获取缓存
```python
redis.get(key,[default])    #返回值：key存在返回数据，不存在返回None
```
其中参数说明
````markdown
key      缓存键名
default  可选，可以设置默认值，默认为None
````

#### 判断缓存是否存在
```python
redis.has(key)   #返回值 ：bool
```
其中参数说明
````markdown
key      缓存键名
````
#### 删除缓存
```python
redis.delete(key)    #返回值 BOOL
```
其中参数说明
````markdown
key      缓存键名
````
