#!/usr/bin/env python3
"""obtain the HTML content of a particular URL and returns it"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def count(fn: Callable) -> Callable:
    """decorator to count number of times url is visited"""

    @wraps(fn)
    def wrapper(url: str) -> str:
        """wrapper function to keep count"""

        # increment count for url visit
        count_key = f"count:{url}"
        r.incr(count_key)

        # set expiration time
        r.expire(count_key, 10)

        # call function and return result
        return fn(url)

    return wrapper


@count
def get_page(url: str) -> str:
    """request a page and returns HTML content"""

    url = "http://slowwly.robertomurray.co.uk"

    return requests.get(url).text
