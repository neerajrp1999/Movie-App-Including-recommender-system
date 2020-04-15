
from MovieLens import MovieLens
from ContentKNNAlgorithm import ContentKNNAlgorithm
from Evaluator import Evaluator
from surprise import NormalPredictor
import socket
import random
import numpy as np

def LoadMovieLensData():
    ml = MovieLens()
    print("Loading movie ratings...")
    data = ml.loadMovieLensLatestSmall()
    print("\nComputing movie popularity ranks so we can measure novelty later...")
    rankings = ml.getPopularityRanks()
    return (ml, data, rankings)
def contentGive(id):    
    np.random.seed(0)
    random.seed(0)
    
    # Load up common data set for the recommender algorithms
    (ml, evaluationData, rankings) = LoadMovieLensData()
    
    # Construct an Evaluator to, you know, evaluate them
    evaluator = Evaluator(evaluationData, rankings)
    
    contentKNN = ContentKNNAlgorithm()
    evaluator.AddAlgorithm(contentKNN, "ContentKNN")
    
    # Just make random recommendations
    Random = NormalPredictor()
    evaluator.AddAlgorithm(Random, "Random")
    
    evaluator.Evaluate(False)
    
    evaluator.SampleTopNRecs(ml,id)
    
def Main():
    host = "127.0.0.6"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((host,port))
    while(True):
         
        mySocket.listen(10)
        conn, addr = mySocket.accept()
        print ("Connection from: " + str(addr))
        data = conn.recv(1024).decode()
        
        print ("from connected  user: " + str(data))
        contentGive(int(data))
        conn.close()
     
if __name__ == '__main__':
    Main()
    #contentGive(2)
