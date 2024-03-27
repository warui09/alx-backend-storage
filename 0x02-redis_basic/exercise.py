#!/usr/bin/env python3
""" task 0 solution """

import redis
from typing import Union, Callable, Optional
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator to count number of times method on Cache has been called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function to increment counter"""
        self._redis.incr(f"{method.__qualname__}")
        return method(self, *args, **kwargs)

    setattr(wrapper, "__calls__", 0)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator to record calls to a method"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function to add calls to history"""

        # convert args to string
        args_str = str(args)

        # log arguments to list
        self._redis.rpush(f"{method.__qualname__}:inputs", args_str)

        # get return value of method and add to list
        result = method(self, *args, **kwargs)
        result_str = str(result)
        self._redis.rpush(f"{method.__qualname__}:outputs", result_str)
        return result_str

    return wrapper

def replay(method: Callable) -> None:
    """prints inputs and outputs of a method"""

    if not method or not hasattr(method, "__self__"):
        return

    data_store = getattr(f"{method.__self__}", "redis", None)

    if not data_store:
        return

    # get list of inputs and outputs
    inputs_keys = f"{data_store.__qualname__}:inputs"
    outputs_keys = f"{data_store.__qualname__):outputs"

    inputs = data_store.lrange(inputs_keys, 0, -1)
    outputs = data_Store.lrange(outputs_keys, 0, -1)

    # print inputs and outputs
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for i in range(len(inputs)):
        print(f"{method.__qualname__}(*({inputs[i].decode('utf-8')})) -> {outputs[i].decode('utf-8')}")

class Cache:
    """cache class"""

    def __init__(self) -> None:
        """class initiliazer"""

        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """put data in Redis using a random key"""

        key = str(uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
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

    @count_calls
    def get_str(self, key: str):
        """return a string"""
        return self.get(key)

    @count_calls
    def get_int(self, key: str):
        """return int"""
        return self.get(key, int)
