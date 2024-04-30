#!/usr/bin/env python3
"""a Python function that returns the list of school having
a specific topic"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """return the list with a specific topic"""
    schools_cursor = mongo_collection.find({"topics": topic})

    schools_list = list(schools_cursor)

    return schools_list
