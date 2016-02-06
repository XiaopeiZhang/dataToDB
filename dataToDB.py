from pymongo import MongoClient
from datetime import datetime

# import: mongoimport --db test --collection restaurants --drop --file primer-dataset.json
# import to server: mongoimport --host mongodb1.example.net --port 37017 --username user --password pass --collection contacts --db marketing --file /opt/backups/mdb1-examplenet.json
# mongoimport --host beckett.casmlab.org --port 22 --username xiaopei --password XXX --collection restaurants --db test --file primer-dataset.json
# https://docs.mongodb.org/getting-started/shell/import-data/

# start driver
# https://docs.mongodb.org/manual/reference/connection-string/
client = MongoClient("mongodb://xiaopei:XXX@beckett.casmlab.org:22/?connectTimeoutMS=300000")
#db = client.primer
db = client.test

# insert
result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

# query
#cursor = db.restaurants.find()
# { <field1>: <value1>, <field2>: <value2>, ... }
# cursor = db.restaurants.find({"borough": "Manhattan"})
# cursor = db.restaurants.find({"address.zipcode": "10075"})
# cursor = db.restaurants.find({"grades.grade": "B"})
# { <field1>: { <operator1>: <value1> } }
# >: cursor = db.restaurants.find({"grades.score": {"$gt": 30}})
# <: cursor = db.restaurants.find({"grades.score": {"$lt": 10}})
# and: cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})
# or: cursor = db.restaurants.find({"$or": [{"cuisine": "Italian"}, {"address.zipcode": "10075"}]})
# sort: cursor = db.restaurants.find().sort([("borough", pymongo.ASCENDING), ("address.zipcode", pymongo.DESCENDING)])
#for document in cursor:
#    print(document)
# update
# one field: result = db.restaurants.update_one({"restaurant_id": "41156888"}, {"$set": {"address.street": "East 31st Street"}})
# result.matched_count, modified_count
# multiple docs: result = db.restaurants.update_many({"address.zipcode": "10016", "cuisine": "Other"}, {"$set": {"cuisine": "Category To Be Determined"}, "$currentDate": {"lastModified": True}})
# replace: result = db.restaurants.replace_one({"restaurant_id": "41704620"}, {"name": "Vella 2", "address": {"coord": [-73.9557413, 40.7720266], "building": "1480", "street": "2 Avenue", "zipcode": "10075"}})
# remove
# result = db.restaurants.delete_many({"borough": "Manhattan"})
# result.deleted_count
# result = db.restaurants.delete_many({})
# db.restaurants.drop()
