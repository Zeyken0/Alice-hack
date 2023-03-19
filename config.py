from pymongo import MongoClient

CLUSTER = MongoClient("mongodb+srv://Alisa:pasword@alisa.cayawc6.mongodb.net/?retryWrites=true&w=majority")
DB = CLUSTER["AlisaBase"]
COLLECTION = DB["users"]