#!/usr/bin/env python3
"""
this is a script that finds
all records basing on the topics
the have
"""


def schools_by_topic(mongo_collection, topic):
    """
    this is a script that finds by the topics
    that a school has
    """
    return mongo_collection.find({"topics": topic})
