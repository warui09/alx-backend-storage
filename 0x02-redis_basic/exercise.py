#!/usr/bin/env python3
""" task 0 solution """

import redis
from typing import Union, Callable, Optional
from uuid import uuid4


class Cache:
    """cache class"""

    def __init__(self) -> None:
        """class initiliazer"""

        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """put data in Redis using a random key"""

        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, int]]] = lambda x: x.decode(),
    ):
        """get data from redis"""

        value = self._redis.get(key)
        if value:
            return fn(value)

        return None

    def get_str(self, key: str):
        """return a string"""

        return self.get(key)

    def get_int(self, key: str):
        """return int"""

        return self.get(key, int)
