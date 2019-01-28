from tinydb import TinyDB, Query

db = TinyDB('db.json')
db.insert({'movies':{1:'Jajantram Mamantram',2:'Mughal-e-Azam',3:'Dil to Pagal Hai',4:'Aashiqui'}})
