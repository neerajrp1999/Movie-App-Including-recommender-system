import socket
file = open("E:\\Neeraj\\presentUser.txt", "r") 
userid=file.read()
file.close()
def LikedBase():
    host = '127.0.0.1'
    port = 5000
    mySocket = socket.socket()
    mySocket.connect((host,port))
    message = userid
    mySocket.send(message.encode())
    mySocket.close()
def SimpleItemCF():
    host = '127.0.0.2'
    port = 5000
    mySocket = socket.socket()
    mySocket.connect((host,port))
    message = userid
    mySocket.send(message.encode())
    mySocket.close()
def SimpleUserCF():
    host = '127.0.0.3'
    port = 5000
    mySocket = socket.socket()
    mySocket.connect((host,port))
    message = userid
    mySocket.send(message.encode())
    mySocket.close()
def ContentRecs():
    host = '127.0.0.6'
    port = 5000
    mySocket = socket.socket()
    mySocket.connect((host,port))
    message = userid
    mySocket.send(message.encode())
    mySocket.close()
def me(r):
    LikedBase()
    SimpleItemCF()
    #SimpleUserCF()
    #ContentRecs()
    r.destroy()
    
