"""
Created by on 2024/7/23.
"""
from flask_caching import Cache
import functools

# from flask import current_app

__author__ = 'JOJO'

class Limiter:
    def __init__(self, cache):
        self.cache = cache

    def limited(self, callback):
        self.limited_callback = callback
        return callback

    def limit(self, key='', key_func=None, time_delta=60):
        def decorator(f):
            key_prefix = "limiter/"

            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                full_key = key_prefix + (key_func() if key_func else key)
                value = self.cache.get(full_key)
                if not value:
                    self.cache.set(full_key, '1', timeout=time_delta)  # Cache the flag, not the time
                    return f(*args, **kwargs)
                else:
                    return self.limited_callback()
            return wrapper
        return decorator




# """
#  Created by 七月 on 2018/1/9.
# """
#
# import functools
# # from flask import current_app
# from werkzeug.contrib.cache import SimpleCache
#
# __author__ = 'JOJO'
#
#
# class Limiter(object):
#     cache = SimpleCache()
#
#     def limited(self, callback):
#         self.limited_callback = callback
#         return callback
#
#     def limit(self, key='', key_func=None, time_delta=60):
#         def decorator(f):
#             key_prefix = "limiter/"
#
#             @functools.wraps(f)
#             def wrapper(*args, **kwargs):
#                 # global cache
#                 full_key = key_prefix + key_func() if key_func else key
#                 value = Limiter.cache.get(full_key)
#                 if not value:
#                     Limiter.cache.set(full_key, time_delta, timeout=time_delta)
#                     return f(*args, **kwargs)
#                 else:
#                     return self.limited_callback()
#             return wrapper
#
#         return decorator
