#!/usr/bin/env python3
"""
is a script that finds and document
in a collection passed in as an argument
"""


def list_all(mongo_collection):
    """
    this is a functiont that returns
    all the documents in a collection
    """
    return mongo_collection.find()
