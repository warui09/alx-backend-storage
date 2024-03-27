#!/usr/bin/env python3
""" task 0 solution """

from __future__ import annotations
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """cache class"""

    def __init__(self: Cache) -> None:
        """class initiliazer"""

        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self: Cache, data: Union[str, bytes, int, float]) -> str:
        """put data in Redis using a random key"""

        key = str(uuid4())
        self._redis.set(key, data)
        return key
