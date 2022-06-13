##print("jhuesHGYUFJH")
import json
import tkinter
from tkinter import *

def main():
    mywin=tkinter.Toplevel(win)
    mywin.geometry('200x200')
    lbl30=tkinter.Label(mywin,text="welcome to main app")
    mywin.mainloop()
def login():
    with open('d:/Project.json') as f:
        dct=json.load(f)
    try:
        
        user=txt.get()
        password=txt2.get()
    
        if(user in dct and dct[user]==password):
            lbl30.configure(text='welcom!!!!',fg="red")
        else:
            lbl30.configure(text='wrong username or password',fg="red")
    except ValueError:
                 pass
   
      
def submit():
    with open ('d:/Project.json')as f:
        dct=json.load(f)
    try:
        user=txt.get()
        password=txt2.get()
    
        if(user in dct):
            lbl30.configure(text="username already exist",fg='red')
            return
        dct[user]=password
        with open ('d:/Project.json ' , 'w') as f:
            json.dump(dct , f)
            lbl30.configure(text="SUBMIT DON !!!",fg='red')
            return
    except ValueError:
        pass
        
        
        


def delete():
    user=txt.get()
    password=txt2.get()

    with open ('d:/Project.json')as f:
        dct=json.load(f)
    if(user in dct and dct[user]==password):
        dct.pop(user)
        with open ('d:/Project.json', 'w') as f:
            json.dump(dct , f)
            lbl30.configure(text="account deleted!",fg="red")
    else:
        lbl30.configure(text="'wrong user or password'!",fg="red")
 
    
    
    
win=tkinter.Tk()
win.title("Project")
win.geometry('250x200+500+200')
lbl=tkinter.Label(win,text='')
lbl.grid(column=0,row=0,sticky=(N, W, E, S))


lbl10=tkinter.Label(win,text="username")
lbl10.grid(column=1, row=1, sticky=E)

lbl20=tkinter.Label(win,text="password")
lbl20.grid(column=1, row=2, sticky=E)

lbl30=tkinter.Label(win,text="label")
lbl30.grid(column=2, row=3)

txt=tkinter.Entry(win,width=20)
txt.grid(column=2, row=1, sticky=(W, E))

txt2=tkinter.Entry(win,width=20)
txt2.grid(column=2, row=2, sticky=(W, E))



btn=tkinter.Button(win,text='LOGIN',command=login)
btn.grid(column=2,row=4)



btn2=tkinter.Button(win,text='SUBMIT',command=submit)
btn2.grid(column=1,row=4)

btn3=tkinter.Button(win,text='Delete',command=delete)
btn3.grid(column=3,row=4)
win.mainloop()
