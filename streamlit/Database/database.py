import certifi
from pymongo import MongoClient

def connectDB(dbName):
  client = MongoClient('mongodb+srv://wonseok:E3kXD7Tta02OWXYT@cluster0.0nbzrz6.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
  db = client.dbName
  
  return db
