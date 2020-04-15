file = open("E:\\Neeraj\\presentUser.txt", "r") 
userid=file.read()
file.close()
def likedbased():
    file = open("E:\\Neeraj\\LikhedBase.txt", "r") 
    r=file.readlines()
    for r1 in r:
        u=r1.find(",")
        if(r1[0:u]==userid):
            file.close()
            s=r1[u+1:-1]
            a="Recomment:"
            i=1
            for w in s:
                if w==",":
                    if(i==1 or i==2 or i==3):
                        a+=w
                        i+=1
                    else:
                        a+=w+"\n"
                        i=1
                else:
                    a+=w
            return a
    file.close()
    return "Nothing is avilable Now"
def SimpleItemCF():
    file = open("E:\\Neeraj\\SimpleItemCFBase.txt", "r") 
    r=file.readlines()
    for r1 in r:
        u=r1.find(",")
        if(r1[0:u]==userid):
            file.close()
            s=r1[u+1:-1]
            a="Recomment:"
            i=1
            for w in s:
                if w==",":
                    if(i==1 or i==2 or i==3):
                        a+=w
                        i+=1
                    else:
                        a+=w+"\n"
                        i=1
                else:
                    a+=w
            return a
    file.close()
    return "Nothing is avilable Now"
def SimpleUserCF():
    file = open("E:\\Neeraj\\SimpleUserCFBase.txt", "r") 
    r=file.readlines()
    for r1 in r:
        u=r1.find(",")
        if(r1[0:u]==userid):
            file.close()
            s=r1[u+1:-1]
            a="Recomment:"
            i=1
            for w in s:
                if w==",":
                    if(i==1 or i==2 or i==3):
                        a+=w
                        i+=1
                    else:
                        a+=w+"\n"
                        i=1
                else:
                    a+=w
            return a
    file.close()
    return "Nothing is avilable Now"
def ContentRecs():
    file = open("E:\\Neeraj\\ContentRecsBase.txt", "r") 
    r=file.readlines()
    for r1 in r:
        u=r1.find(",")
        if(r1[0:u]==userid):
            file.close()
            s=r1[u+1:-1]
            a="Recomment:"
            i=1
            for w in s:
                if w==",":
                    if(i==1 or i==2 or i==3):
                        a+=w
                        i+=1
                    else:
                        a+=w+"\n"
                        i=1
                else:
                    a+=w
            return a
    file.close()
