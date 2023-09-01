#!/usr/bin/env python3
"""
a script to write strings
to redis
"""

from uuid import uuid4
import redis
from typing import Union


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    def __init__(self):
        """
        the constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """
        this is a method to store into
        the database
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
