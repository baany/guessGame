import random
#from tinydb import TinyDB, Query
from retrieveMovieDict import getMovieFromDict

#db = TinyDB('db.json')

#movieList = ['Jajantram Mamantram','Mughal-e-Azam','Dil to Pagal Hai', 'Aashiqui']
#movieRandom = random.choice(movieList)
movieRandom = getMovieFromDict()
mediaM = movieRandom.lower()
media = list(mediaM)
#print (media)

guessMedia = ''
lengMedia = len(media)
flag = 0
for item in range(0,lengMedia):
    if(media[item]=='a' or media[item]=='e' or media[item]=='i' or media[item]=='o' or media[item]=='u'):
        guessMedia = guessMedia+media[item]
    elif(media[item]=='/' or media[item]==':' or media[item]=='-' or media[item]==' '):
        guessMedia = guessMedia+'/'
        mediaM = mediaM.replace(media[item], '/')
    else:
        guessMedia = guessMedia+'_'

attempts = 9
print ("Attempts : ",attempts)
print (guessMedia)

while(attempts!=0):
    character = input("Enter a character : ")
    replaceChar = []
    flag = 0
    for item in range(0,lengMedia):
        if (media[item]==character.lower()):
            replaceChar = list(guessMedia)
            replaceChar[item]=character.lower()
            guessMedia = ''.join(replaceChar)
            flag=1
        else:
            pass
    if(flag==0):
        attempts=attempts-1
    print ('\n')
    print ("Attempts : ",attempts)
    print (guessMedia)
    #print (mediaM)
    if (guessMedia == mediaM.lower() and attempts!=0):
        print ("You Won!!")
        break
    elif(attempts==0) :
        print ("You lose!!")
        print ("The movie name was --> ", movieRandom)
        break
