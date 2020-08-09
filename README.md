# python_cache
基于thinkphp的文件缓存来实现的一种文件缓存，自己来练练手，慢慢的去完善


##文件缓存的使用
### 导入包
```python
from  cache import RunTime,FileCache
```
其中runtime为运行缓存目录，FileCache为文件缓存
###配置
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
#####options选项配置说明

| 字段 | 说明 | 数据类型 |默认值 |
| ----  |----  |----|----|
| options['expire']  | 缓存有效时间 |Number| 0(永久缓存)
| options['cache_subdir'] |  是否开启缓存子目录| Bool | True
| options['prefix']  | 缓存前缀 |str|''
| options['path']  | 缓存路径 |str|''
| options['hash_type']  | 缓存文件hash方式|str| md5
| options['data_compress']  | 缓存数据是否压缩 |bool| False

###方法
####初始化化
```python
cache = cache.Cache([options])
```
其中options是可选自定义配置的，
####设置缓存
````python
cache.set(cacheName, cacheValue, expire)
````
````markdown
其中参数说明

cacheName      为缓存的名称

cacheValue     为缓存的值

expire         可选，缓存的有效期`
````
####获取缓存
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