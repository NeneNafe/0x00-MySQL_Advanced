#!/usr/bin/env python3
"""A class Cache class. It has an init method that stores
an instance of the Redis client as a private variable"""


import redis
import uuid
from typing import Union


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
