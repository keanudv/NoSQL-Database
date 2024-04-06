#Name: Keanu Valencia
#Class: ICS 385
#Date: 4/6/2024
#Description: Uses a NoSQL document database to store three documents, update one document, then deletes all documents.

#imports the packages.
import pymongo

#connects to the local server.
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#creates a database called myNewDatabase.
mydb = myclient["myNewDatabase"]

#creates a collection, or table, called customers.
mycol = mydb["customers"]

#creates three documents, or records, in JSON format.
customerOne = {
    "firstname": "Steph",
    "lastname": "Curry",
    "age": 30,
    "gender": "Male",
    "email": "stephcurry30@hawaii.edu"
}
customerTwo = {
    "firstname": "Trae",
    "lastname": "Young",
    "age": 11,
    "gender": "Male",
    "email": "traeyoung11@hawaii.edu"
}
customerThree = {
    "firstname": "Caitlin",
    "lastname": "Clark",
    "age": 22,
    "gender": "female",
    "email": "cclark22@hawaii.edu"
}

#inserts the three documents into the customers collection.
x = mycol.insert_many([customerOne, customerTwo, customerThree])

#uses a For Loop to find and print all three documents.
for x in mycol.find():
  print(x)

#updates one document.
myQuery = {"age": 30}
newValues = {"$set": {"age": 34}}
mycol.update_one(myQuery, newValues)