#-*- coding:utf8 -*-

import datetime
import time
import inspect
import functools

def cache(exp=0):
    def _cache(fn):
        cache_dict = {}
        names = set()
        @functools.wraps(fn)
        def wrap(*args, **kwargs):
            key = []
            params = inspect.signature(fn).parameters
            for k, arg in enumerate(args):
                name = list(params.keys())[k]
                key.append((name,arg))
                names.add(name)
            key.extend(kwargs)
            for k, v in params.items():
                if k not in names:
                    key.append((k,v.deault))
            key.sort(key=lambda x: x[0])
            key = '&'.join(['{}={}'.format(name, arg) for name, arg in key])
            print(key)
            if key in cache_dict.keys():
                if datetime.datetime.now().timestamp() - cache_dict[key][1] < exp or exp == 0: # 缓存时间为exp,exp的值为0的话永不过期
                    print('cache hit')
                    return cache_dict[key]
            ret = fn(*args, **kwargs)
            run_time = datetime.datetime.now().timestamp()
            cache_dict[key] = (ret,run_time)
            print('cache miss')
            return ret
        return wrap
    return _cache

@cache(4) # 定义一个缓存4秒的函数
def add(x,y):
    return x + y

add(1,2)
add(1,2)
time.sleep(5)
add(1,2)

@cache() # 定义一个永久缓存的函数
def add1(x,y):
    return x + y

add1(1,2)
add1(1,2)
time.sleep(5)
add1(1,2)