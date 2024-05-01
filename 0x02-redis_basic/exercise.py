#!/usr/bin/env python3
"""A class Cache class. It has an init method that stores
an instance of the Redis client as a private variable"""


import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """a class that has all the functions required"""
    def __init__(self):
        self._redis = redis.Redis()
        self.flushdb()

    def flushdb(self):
        """flushes the redis database"""
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores the input data in Redis using randomly"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """take a key string argument and an optional
        Callable argument named fn"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """parametrizes cache.get with the correct conversion function"""
        variable = self._redis.get(key)
        return variable.decode("UTF-8")

    def get_int(self, key: str) -> int:
        """parametrizes cache.get with the correct conversion function"""
        variable = self._redis.get(key)
        try:
            variable = int(variable.decode("UTF-8"))
        except Exception:
            variable = 0
        return variable
