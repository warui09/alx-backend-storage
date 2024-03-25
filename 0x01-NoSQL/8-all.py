#!/usr/bin/env python3
""" task 8 solution """

import pymongo


def list_all(mongo_collection):
    """lists all documents in a mongo collection"""

    return mongo_collection.find()
