from pymongo import MongoClient

try:
    # client = MongoClient("mongodb+srv://notes_admin:notes123@notes.clbah.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    #client = MongoClient("mongodb://localhost:27017")
    client = MongoClient("mongodb+srv://ciplax:ciplax@cluster0.wpfju.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.notes_api
    print("Berhasil terhubung ke MongoDB...")
except: 
    print("Gagal terhubung ke MongoDB...")

collection_name = db['notes']