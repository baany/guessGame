from tinydb import TinyDB, Query
import random

db = TinyDB('db.json')
moviesDict = db.all()[0]['movies']

def getMovieFromDict():
    #print (moviesDict)
    #print (len(moviesDict))
    choiceInt = random.randint(1,len(moviesDict))
    #print (choiceInt)
    movie2guess = moviesDict[str(choiceInt)]
    return (movie2guess)

