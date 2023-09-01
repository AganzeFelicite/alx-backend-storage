#!/usr/bin/env python3
"""
a script to write strings
to redis
"""

from uuid import uuid4
import sys
import redis
from typing import Union, Optional, Callable
from functools import wraps


Types = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    my wrapper here
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        it increments the count
        every time its called
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    add its input parameters to one list
    in redis, and store its output into another list.
    :param method:
    :return:
    """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapp """
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return res

    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls of a particular function"""
    method_key = method.__qualname__
    inputs, outputs = method_key + ':inputs', method_key + ':outputs'
    r = redis.Redis()
    method_count = r.get(method_key).decode('utf-8')
    print(f'{method_key} was called {method_count} times:')
    IOTuple = zip(r.lrange(inputs, 0, -1), r.lrange(outputs, 0, -1))
    for inp, outp in list(IOTuple):
        attr, data = inp.decode("utf-8"), outp.decode("utf-8")
        print(f'{method_key}(*{attr}) -> {data}')


class Cache:
    def __init__(self):
        """
        the constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Types) -> str:
        """
        this is a method to store into
        the database
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Types:
        """
        this method returns stored
        values from redis and convert
        the b to utf-8
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self: bytes) -> str:
        """
        this method convert a byte back
        to utf-8
        """
        return self.decode("utf-8")

    def get_int(self: bytes) -> str:
        """
        this converts a byte back to
        integer
        """
        return self.from_bytes(self, sys.byteorde)
