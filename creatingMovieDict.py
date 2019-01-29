from tinydb import TinyDB, Query

db = TinyDB('db.json')
#db.insert({'movies':{1:'Jajantram Mamantram',2:'Mughal-e-Azam',3:'Dil to Pagal Hai',4:'Aashiqui'}})
moviesDict = db.all()[0]['movies']
print (moviesDict)
leng = len(moviesDict)
#print (leng)
movie2add = input("Enter the movie name : ")
moviesDict.update({leng+1:movie2add})
db.purge()
db.insert({'movies':moviesDict})
print (db.all())
