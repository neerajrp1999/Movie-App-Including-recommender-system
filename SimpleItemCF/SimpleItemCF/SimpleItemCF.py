
from MovieLens import MovieLens
from surprise import KNNBasic
import heapq
from collections import defaultdict
from operator import itemgetter
import socket
def simpleItemCFGive(id):
    testSubject = str(id)
    k = 10
    
    ml = MovieLens()
    data = ml.loadMovieLensLatestSmall()
    
    trainSet = data.build_full_trainset()
    
    sim_options = {'name': 'cosine',
                   'user_based': False
                   }
    
    model = KNNBasic(sim_options=sim_options)
    model.fit(trainSet)
    simsMatrix = model.compute_similarities()
    
    testUserInnerID = trainSet.to_inner_uid(testSubject)
    
    # Get the top K items we rated
    testUserRatings = trainSet.ur[testUserInnerID]
    kNeighbors = heapq.nlargest(k, testUserRatings, key=lambda t: t[1])
    
    # Get similar items to stuff we liked (weighted by rating)
    candidates = defaultdict(float)
    for itemID, rating in kNeighbors:
        similarityRow = simsMatrix[itemID]
        for innerID, score in enumerate(similarityRow):
            candidates[innerID] += score * (rating / 5.0)
        
    # Build a dictionary of stuff the user has already seen
    watched = {}
    for itemID, rating in trainSet.ur[testUserInnerID]:
        watched[itemID] = 1
        
    # Get top-rated items from similar users:
    s="\n"+str(id)
    pos = 0
    for itemID, ratingSum in sorted(candidates.items(), key=itemgetter(1), reverse=True):
        if not itemID in watched:
            movieID = trainSet.to_raw_iid(itemID)
            s+=","+ml.getMovieName(int(movieID))
            pos += 1
            if (pos > 10):
                break
    file = open("E:\\Neeraj\\SimpleItemCFBase.txt", "r") 
    alld=file.readlines()
    file.close()
    file1 = open("E:\\Neeraj\\SimpleItemCFBase.txt", "w")
    for r1 in alld:
        print(r1)
        u=r1.find(",")
        if(r1[0:u]==str(id)):
                pass
        else:
            file1.write(r1)
    file1.write(s)
    file1.close()
    print ("\nDone")
def Main():
    host = "127.0.0.2"
    port = 5000
    
    mySocket = socket.socket()
    mySocket.bind((host,port))
    while(True):
        mySocket.listen(10)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        
        print ("from connected  user: " + str(data))
        simpleItemCFGive(int(data))
        conn.close()
     
if __name__ == '__main__':
    Main()
    #simpleItemCFGive(2)
   


