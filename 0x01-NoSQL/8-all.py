#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""


import pymongo


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    documents = list(mongo_collection.find())

    return documents
