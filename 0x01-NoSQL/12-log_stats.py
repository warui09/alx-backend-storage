#!/usr/bin/env python3
""" task 12 solution """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("localhost")
    db = client.logs

    call = db.command("dbstats")
    objects = call["objects"]
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{objects} logs")
    print("Methods:")
    for method in methods:
        count = len(list(db.nginx.find({"method": method})))
        print(f"\tmethod {method}: {count}")

    status_checks = len(list(db.nginx.find({"method": "GET", "path": "/status"})))
    print(f"{status_checks} status checks")
