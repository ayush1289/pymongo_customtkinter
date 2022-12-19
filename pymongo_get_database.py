from pymongo import MongoClient
def get_database():
   CONNECTION_STRING = "mongodb+srv://ayush12:12@notes.scnzyea.mongodb.net/notes?retryWrites=true&w=majority"
   client = MongoClient(CONNECTION_STRING)
   return client['notes_db']
  
if __name__ == "__main__":   
   dbname = get_database()