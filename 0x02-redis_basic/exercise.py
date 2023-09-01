#!/usr/bin/env python3
"""
a script to write strings
to redis
"""

from uuid import uuid4
import sys
import redis
from typing import Union, Optional, Callable


Types = Union[str, bytes, int, float]


class Cache:
    def __init__(self):
        """
        the constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
