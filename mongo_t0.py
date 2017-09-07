from pymongo import MongoClient
from bson.son import SON

db = MongoClient("mongodb://localhost:27017").aggregation_example
collection = db.things
pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
   {"$sort": SON([("count", -1), ("_id", -1)])}
    ]

print(list(db.things.aggregate(pipeline)))

#print(list(db.things.aggregate([{'$sample': {'size': 1 }}])))
winner = [ d for d in collection.aggregate([{'$sample': {'size': 1 }}])][0]
print(winner)