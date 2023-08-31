#!/usr/bin/env python3
"""
this is a script that insert into a given
collection values using pymongo in the main
file
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert new documents in the kwargs
    to the the mongo db collection
    """
    newDocuments = mongo_collection.insert_one(kwargs)
    return newDocuments.inserted_id
