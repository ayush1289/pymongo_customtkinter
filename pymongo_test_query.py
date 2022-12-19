from pandas import DataFrame
from pymongo_get_database import get_database
import pandas as pd

dbname = get_database()
collection_name = dbname["notes1"]
 
item_details = collection_name.find()
# dikkat to yaha pr hai items_df list show kr raha h or vaha login me specific index de diya h
items_df = DataFrame(item_details)

# val=items_df['password'].where(items_df['email']==('ayushshankarpurkar11@gmail.com\n'))
val=items_df['password'].where(items_df['email']==('ayush'))
# print(val)
# for i in items_df.where(items_df['email'=='ayush'] and items_df['password']=='123'):
#     if i=="123":
#         print("hi")
#     else:
#         print(i) 



