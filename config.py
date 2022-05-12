import pymongo
import certifi



con_str = "mongodb+srv://albert:G1.izmorules@cluster0.gf6xm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("PescadoFishing")