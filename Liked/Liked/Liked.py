from MovieLens import MovieLens
from surprise import SVD
import socket
print("Ok")
def BuildAntiTestSetForUser(testSubject, trainset):
    fill = trainset.global_mean

    anti_testset = []
    
    u = trainset.to_inner_uid(str(testSubject))
    
    user_items = set([j for (j, _) in trainset.ur[u]])
    anti_testset += [(trainset.to_raw_uid(u), trainset.to_raw_iid(i), fill) for
                             i in trainset.all_items() if
                             i not in user_items]
    return anti_testset

def Liked(id):
	testSubject = id
	ml = MovieLens()

	print("Loading movie ratings...")
	data = ml.loadMovieLensLatestSmall()

	userRatings = ml.getUserRatings(testSubject)
	loved = []
	hated = []
	for ratings in userRatings:
		if (float(ratings[1]) > 4.0):
			loved.append(ratings)
		if (float(ratings[1]) < 3.0):
			hated.append(ratings)

	print("\nUser ", testSubject, " loved these movies:")
	for ratings in loved:
		print(ml.getMovieName(ratings[0]))
	print("\n...and didn't like these movies:")
	for ratings in hated:
		print(ml.getMovieName(ratings[0]))

	print("\nBuilding recommendation model...")
	trainSet = data.build_full_trainset()

	algo = SVD()
	algo.fit(trainSet)

	print("Computing recommendations...")
	testSet = BuildAntiTestSetForUser(testSubject, trainSet)
	predictions = algo.test(testSet)

	recommendations = []

	print ("\nWe recommend:")
	for userID, movieID, actualRating, estimatedRating, _ in predictions:
		intMovieID = int(movieID)
		recommendations.append((intMovieID, estimatedRating))

	recommendations.sort(key=lambda x: x[1], reverse=True)
	s="\n"+str(id)
	for ratings in recommendations[:10]:
		s+=","+ml.getMovieName(ratings[0])
	file = open("E:\\Neeraj\\LikhedBase.txt", "r") 
	alld=file.readlines()
	file.close()
	file1 = open("E:\\Neeraj\\LikhedBase.txt", "w")
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
    host = "127.0.0.1"
    port = 5000
    
    mySocket = socket.socket()
    mySocket.bind((host,port))
    while(True):
        mySocket.listen(10)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        
        print ("from connected  user: " + str(data))
        Liked(int(data))
        conn.close()
     
if __name__ == '__main__':
    Main()
    #Liked(2)
