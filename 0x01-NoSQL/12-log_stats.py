#!/usr/bin/env python3
"""a Python script that provides some stats about Nginx logs"""


from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def nginx_log_stats(mongo_collection, option=None):
    """ script that provides some stats about Nginx logs stored in MongoDB
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        nginx_log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    nginx_log_stats(nginx_collection)
