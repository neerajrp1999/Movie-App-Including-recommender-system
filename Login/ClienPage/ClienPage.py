import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as m
def Register(tk):
    tk.destroy()
    window = tkinter.Tk()
    window.title("Welcome to TutorialsPoint")
    window.geometry('300x200')
    a = Label(window ,text = "User ID").grid(row = 0,column = 0)
    b = Label(window ,text = "Email Id").grid(row = 1,column = 0)
    c = Label(window ,text = "Contact Number").grid(row = 2,column = 0)
    d = Label(window ,text = "Password").grid(row = 3,column = 0)
    file = open("E:\\Neeraj\\NextID.txt", "r") 
    r=file.read()
    id = Label(window ,text = r).grid(row = 0,column = 1)
    file.close()
    b1 = Entry(window)
    b1.grid(row = 1,column = 1,sticky=W)
    c1 = Entry(window)
    c1.grid(row = 2,column = 1,sticky=W)
    d1 = Entry(window)
    d1.grid(row = 3,column = 1,sticky=W)
    def registerSubmit():
        file = open("E:\\Neeraj\\NextID.txt", "w")
        nextid=int(r)+1
        file.write(str(nextid))
        file.close()
        print(nextid)
        file1 = open("E:\\Neeraj\\test.txt", "a") 
        file1.write("\n"+r+","+d1.get()+","+b1.get()+","+c1.get())
        file1.close()
        m.showinfo("Done","Registation Done")
        Login(window)
    btn = ttk.Button(window ,text="Submit", command=registerSubmit).grid(row=4,column=0)
    btn = ttk.Button(window ,text="Back", command=lambda:Login(window)).grid(row=5,column=0)
    window.mainloop()
def Login(tk):
    global nameEL
    global pwordEL
    global rootA
    tk.destroy()
    rootA = tkinter.Tk()
    rootA.title('Login')
    instruction = Label(rootA, text='Please Login\n')
    instruction.grid(sticky=E)

    nameL = Label(rootA, text='User ID: ')
    pwordL = Label(rootA, text='Password: ')
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)

    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
    def checkLogin():
        s=nameEL.get()
        s2=pwordEL.get().strip()
        l=len(s2)
        file = open("E:\\Neeraj\\test.txt", "r") 
        r=file.readlines()
        file.close()
        i=0
        for r1 in r:
            if r1[0]==s and r1[2:2+l].strip()==s2:
                i=1
                break
        if i==1:
            file1 = open("E:\\Neeraj\\presentUser.txt", "w")
            file1.write(s)
            file1.close()
            rootA.destroy()
            #exec(open("Home.py").read())
            import Home
        else:
            m.showerror("Invalide","Invalide use")
    loginB = Button(rootA, text='Login' ,command=lambda:checkLogin())
    loginB.grid(columnspan=2, sticky=W)
    
    RB = Button(rootA, text='New Registration',command=lambda:Register(rootA))
    RB.grid(columnspan=2, sticky=W)
    rootA.mainloop()
tk = tkinter.Tk()
Login(tk)

