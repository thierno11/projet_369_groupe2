from pymongo import MongoClient

# Connexion MongoDB (localhost)
login_mongo = MongoClient("mongodb://localhost:27017/")

# Base et collection
db = login_mongo["datasetMongo"]



def get_data(db,collection): 
    
    eleves_collection = db[collection]

    return list(eleves_collection.find())



matieres = get_data(db,"matieres") 
cours = get_data(db,"cours")
eleves = get_data(db,"eleves")
enseignants = get_data(db,"enseignants")
etablissements = get_data(db,"etablissements")
enseignants = get_data(db,"enseignants")
notes = get_data(db,"notes")
regions = get_data(db,"regions")
presences = get_data(db,"presences")

# print(regions)commit