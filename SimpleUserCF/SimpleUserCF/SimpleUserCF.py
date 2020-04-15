
from MovieLens import MovieLens
from surprise import KNNBasic
import heapq
from collections import defaultdict
from operator import itemgetter
import socket
def simpleUserCFGive(id):
    testSubject = str(id)
    k = 10
    
    # Load our data set and compute the user similarity matrix
    ml = MovieLens()
    data = ml.loadMovieLensLatestSmall()
    
    trainSet = data.build_full_trainset()
    
    sim_options = {'name': 'cosine',
                   'user_based': True
                   }
    
    model = KNNBasic(sim_options=sim_options)
    model.fit(trainSet)
    simsMatrix = model.compute_similarities()
    
    # Get top N similar users to our test subject
    # (Alternate approach would be to select users up to some similarity threshold - try it!)
    testUserInnerID = trainSet.to_inner_uid(testSubject)
    similarityRow = simsMatrix[testUserInnerID]
    
    similarUsers = []
    for innerID, score in enumerate(similarityRow):
        if (innerID != testUserInnerID):
            similarUsers.append( (innerID, score) )
    
    kNeighbors = heapq.nlargest(k, similarUsers, key=lambda t: t[1])
    
    # Get the stuff they rated, and add up ratings for each item, weighted by user similarity
    candidates = defaultdict(float)
    for similarUser in kNeighbors:
        innerID = similarUser[0]
        userSimilarityScore = similarUser[1]
        theirRatings = trainSet.ur[innerID]
        for rating in theirRatings:
            candidates[rating[0]] += (rating[1] / 5.0) * userSimilarityScore
        
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
    file = open("E:\\Neeraj\\SimpleUserCFBase.txt", "r") 
    alld=file.readlines()
    file.close()
    file1 = open("E:\\Neeraj\\SimpleUserCFBase.txt", "w")
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
    host = "127.0.0.3"
    port = 5000
    
    mySocket = socket.socket()
    mySocket.bind((host,port))
    while(True):
        mySocket.listen(10)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        
        print ("from connected  user: " + str(data))
        simpleUserCFGive(int(data))
        conn.close()
     
if __name__ == '__main__':
    Main()
    #simpleUserCFGive(2)


