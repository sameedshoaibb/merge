#!https://realpython.com/introduction-to-mongodb-and-python/
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client['pymongo_test']
posts = db.posts

name= raw_input("What is your name?")
father_name= raw_input("What is your father name?")

post_data = {'Name': name, 'father_name': father_name}


result = posts.insert_one(post_data)


import pymongo

myclient = pymongo.MongoClient()
db = myclient["pymongo_test"]
posts = db.posts

for x in posts.find():
  print(x) 
