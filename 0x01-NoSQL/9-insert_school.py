#!/usr/bin/env python3
""" task 9 solution """

import pymongo

def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """

    new_school = {}

    for key, value in kwargs.items():
        new_school.update({key: value})

    mongo_collection.insert_one(new_school)    
