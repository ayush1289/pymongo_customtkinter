from pymongo import MongoClient
from dateutil import parser
from pandas import DataFrame
import pandas as pd

def get_database():
   CONNECTION_STRING = "mongodb+srv://ayush12:12@notes.scnzyea.mongodb.net/notes?retryWrites=true&w=majority"
   client = MongoClient(CONNECTION_STRING)
   return client['notes_db']
   
dbname = get_database()
collection_name = dbname["notes1"]


expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
  
if __name__ == "__main__":   
   dbname = get_database()




