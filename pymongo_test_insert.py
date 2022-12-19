from dateutil import parser
from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["notes1"]

expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
