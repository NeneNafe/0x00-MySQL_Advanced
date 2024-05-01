#!/usr/bin/env python3
"""This function implements an expiring web cache and tracker"""


import requests
import redis
import time
from functools import wraps

store = redis.Redis()


def cache_with_expiration(method):
    """A decorator that counts the times a Url is accessed"""
    @wraps(method)
    def wrapper(url):
        cache_key = "cached:" + url
        cached_data = store.get(cache_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cache_key, html)
        store.expire(cache_key, 10)
        return html
    return wrapper


@cache_with_expiration
def get_page(url: str) -> str:
    """returns an html content"""
    re = requests.get(url)
    return re.text
