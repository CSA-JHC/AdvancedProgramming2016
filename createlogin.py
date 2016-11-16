from tkinter import *
from tkinter import ttk
import codecs

def info(*args):
    en=open('rot13.txt','r')
    for line in en:
        i=line.split()
        e=[]
        e.append(codecs.decode(i[0],'rot13'))
        e.append(codecs.decode(i[1],'rot13'))
        j=' '.join(e)
        user=[]
        user.append(username.get())
        user.append(password.get())
        x=' '.join(user)
        if x==j:
            sf.set('Login Successful')
            en.close()
            break
        elif x!=j:
            sf.set('Access Denied')
    en.close()


root=Tk()
root.title("Login")

loginframe=Frame(root, bd=2, padx=25, pady=25, relief="sunken")
loginframe.pack(side=TOP)

username=StringVar()
password=StringVar()
sf=StringVar()

ttk.Label(loginframe, text="Username: ").grid(column=1, row=1, sticky=W)
ttk.Label(loginframe, text="Password: ").grid(column=1, row=2, sticky=W)

un_entry=ttk.Entry(loginframe, width=15, textvariable=username)
un_entry.grid(column=2, row=1, sticky=(W,E))

pw_entry=ttk.Entry(loginframe, width=15, textvariable=password)
pw_entry.grid(column=2, row=2, sticky=(W,E))

buttonframe=Frame(root, height=200, padx=50, pady=50, relief="sunken")
buttonframe.pack(side=RIGHT)
ttk.Button(buttonframe, text="Login", command=info).grid(column=2, row=3, sticky=E)

answerframe=Frame(root, height=200, padx=50, pady=50, relief="sunken")
answerframe.pack(side=LEFT)
l1=ttk.Label(answerframe, textvariable=sf).grid(column=2, row=3, sticky=(W,E))

root.bind('<Return>', info)
root.mainloop()
