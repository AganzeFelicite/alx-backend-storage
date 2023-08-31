#!/usr/bin/env python3
"""
this is a script to update the topic in document
of a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    this is a script to update a document in
    the mongo db collection school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
