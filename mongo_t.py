from pymongo import MongoClient


db = MongoClient("mongodb://localhost:27017").aggregation_example
result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
                                 {"x": 2, "tags": ["cat"]},
                                 {"x": 2, "tags": ["mouse", "cat", "dog"]},
                                 {"x": 3, "tags": []}])
result.inserted_ids