#!/usr/bin/env python3
""" task 12 solution """

from pymongo import MongoClient


def show_stats():
    """provides some stats about Nginx logs stored in MongoDB"""

    client = MongoClient("localhost")
    db = client.logs

    call = db.command("dbstats")
    objects = call["objects"]
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{objects} logs")
    print("Methods:")
    for method in methods:
        count = len(list(db.nginx.find({"method": method})))
        print("method {}: {}".format(method, count))

    status_checks = len(list(db.nginx.find({"method": "GET", "path": "/status"})))
    print(f"{status_checks} status checks")


if __name__ == "__main__":
    """run script directly"""

    show_stats()
