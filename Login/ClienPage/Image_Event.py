import tkinter
import csv
from tkinter import *
from tkinter import ttk
def Save(m,r,root):
    root.destroy()
    file = open("E:\\Neeraj\\presentUser.txt", "r") 
    userid=file.read()
    file.close()
    
    with open('E:\\Neeraj\\ml-latest-small\\ratings.csv','a') as f:
        writer=csv.writer(f)
        writer.writerow([int(userid),m,float(r),1260759144])
        
    #b()
def TakeRating(MovieID):
    root = Tk()
    root.geometry('200x200')
    l=Label(root,text="Thank You for Wathing\nGive Rating").pack()
    rate = Entry(root)
    rate.pack()
    b1=Button(root, text="Ok", command=lambda:Save(MovieID,rate.get(),root))
    b1.pack()
    root.mainloop()
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
