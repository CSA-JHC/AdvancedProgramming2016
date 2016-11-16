from tkinter import *
from tkinter import ttk
import getpass
import csv
import time
import os
import re
import hashlib
# import RPi.GPIO as io
from datetime import datetime
# io.setmode(io.BCM)
# pir_pin = 24
# power_pin = 27
# os.system("clear")
# io.setup(pir_pin, io.IN)
# io.setup(power_pin, io.OUT)
# io.output(power_pin, False)
# PERIOD_OF_TIME = 1800

#don't do anything basically
def IForgot(*args):
    loginabout.set("You Forgot!")
#if about is clicked
def About(*args):
    loginabout.set("About stuff...")
def clear(*args):
    #clear screen
    pw_entry.delete(0, END)
    un_entry.delete(0, END)

#checks with file
def loginoffline(*args):
    try:
        f2 = open('hashd.csv', 'r')
        f = open("Logins.txt","a")
        students=csv.reader(f2)
        username=un_entry.get()
        password=pw_entry.get()
        username_rowgetnumyo=2 #change host_row to the corresponding row - 1 (ie; row 45, put in 44) in google's csv
        password_rowgetnum=3 #master_row to the schools student list
        salt="gnuvie:^)"
        for hosts_rowyo in students:
            row = 1
            username=username.replace("@chaparralstaracademy.com","")
            hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].replace("@chaparralstaracademy.com","")
            hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].zfill(4)
            #print(str(hashlib.sha256(username.encode("UTF-8")).hexdigest())+" username "+hosts_rowyo[username_rowgetnumyo]+"\n"+str(hashlib.sha256(password.encode("UTF-8")).hexdigest())+" password "+hosts_rowyo[password_rowgetnum])
            if(username=="displayport:^)"):
                exit()
            if (hashlib.md5((salt+username).encode("UTF-8")).hexdigest() == hosts_rowyo[username_rowgetnumyo]) & (hashlib.md5((salt+password).encode("UTF-8")).hexdigest() == hosts_rowyo[password_rowgetnum]):
##                loginabout.set("Logging in."),
##                time.sleep(1)
##                print(".", end=""),
##                time.sleep(1)
##                print(".")
##                time.sleep(3)
                #os.system("clear")
                #loginabout.set("Logging in complete! Plug in your chromebook now;")
                f.write(username+" "+str(datetime.now())+"\n")
                f.close()
                start = time.time()
                while True :
                    # io.output(power_pin, True)
                    #
                    # if time.time() > start + PERIOD_OF_TIME:
                    #     print("POWER OFF")
                    #     time.sleep(1)
                    #     io.output(power_pin, False)
                    #     time.sleep(3)
                    #     loginoffline()
                    #     break
                    loginabout.set("Logging in complete! Plug in your chromebook now.")
                    #loginabout.set("It works!")
                    break
                clear()
                break
            if (hashlib.md5((salt+username).encode("UTF-8")).hexdigest() != hosts_rowyo[username_rowgetnumyo]) & (hashlib.md5((salt+password).encode("UTF-8")).hexdigest() != hosts_rowyo[password_rowgetnum]):

##        print("Logging in."),
##        time.sleep(1)
##        print(".", end=""),
##        time.sleep(1)
##        print(".")
##        time.sleep(3)
        #os.system("clear")
                loginabout.set("Error logging in, please try again! ")
        #loginoffline(*args)
        f2.close()
        f.close()
    except KeyboardInterrupt:
        loginabout.set("Error, please try again! ")
        loginoffline(*args)
        clear()



                
root=Tk()
root.title('Login')

menuframe=Menu(root)
root.config(menu=menuframe)

#exit menu (to exit)
#exitmenu=Menu(menuframe)
#menuframe.add_cascade(label="Options", menu=exitmenu)
#exitmenu.add_command(label="Exit", command=root.quit)

#help menu (for help)
#helpmenu=Menu(menuframe)
#menuframe.add_cascade(label="Help", menu=helpmenu)
#helpmenu.add_command(label="Forgot Password...", command=IForgot)
#helpmenu.add_command(label="About", command=About)

#frame for entries
mainframe=ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#labels
username=StringVar()
password=StringVar()
loginabout=StringVar()

#password and username entry, label, and login button
ttk.Label(mainframe, text="Username: ").grid(column=1, row=1, sticky=W)
un_entry=ttk.Entry(mainframe, width=30, textvariable=username)
un_entry.grid(column=2, row=1, sticky=(W,E))
ttk.Label(mainframe, text="Password: ").grid(column=1, row=2, sticky=W)
pw_entry=ttk.Entry(mainframe, width=30, textvariable=password)
pw_entry.grid(column=2, row=2, sticky=(W,E))
pw_entry.config(show='*') #don't show pw when typing
button=ttk.Button(mainframe, text="Login", command=loginoffline).grid(column=2, row=3, sticky=N) #login button

#label showing whether you put something in
correct=ttk.Label(mainframe, textvariable=loginabout).grid(column=2, row=4, sticky=E)
##ttk.Label(mainframe,textvariable=about).grid(column=3, row=3, sticky=N)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>', loginoffline)
root.mainloop() #do it again
