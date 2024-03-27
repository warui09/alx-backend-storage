#!/usr/bin/env python3
""" task 15 solution """

from pymongo import MongoClient


def show_stats():
    """provides some stats about Nginx logs stored in MongoDB"""

    client = MongoClient("localhost")
    db = client.logs

    call = db.command("dbstats")
    objects = call["objects"]
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    pipeline = [
        {"$group": {"_id": "$ip", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
        {"$limit": 10},
    ]

    ips = db.nginx.aggregate(pipeline)

    print(f"{objects} logs")
    print("Methods:")
    for method in methods:
        count = len(list(db.nginx.find({"method": method})))
        print("\tmethod {}: {}".format(method, count))

    status_checks = len(list(db.nginx.find({"method": "GET", "path": "/status"})))
    print(f"{status_checks} status checks")

    print("IPs:")
    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("total")))


if __name__ == "__main__":
    """run script directly"""

    show_stats()
