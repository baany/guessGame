from tinydb import TinyDB, Query

db = TinyDB('db.json')
moviesDict = db.all()[0]['movies']
print (moviesDict)
print (len(moviesDict))
for item in moviesDict:
    print (moviesDict[item])
