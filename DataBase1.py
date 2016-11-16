from tkinter import *
from tkinter import ttk

def write(*args):
    try:
        #open and append to file
        file=open('info.txt','a')
        #if yes is selected write info
        if y.get()==1 and n.get()==0:
            file.write(fname.get()+','+lname.get()+','+str(rb.get())+','+state.get()+','+str(y.get())+'\n')
        #if no is selected write info
        elif y.get()==0 and n.get()==1:
            file.write(fname.get()+','+lname.get()+','+str(rb.get())+','+state.get()+','+str(n.get())+'\n')
        #clear the screen
        fname.delete(0,END)
        lname.delete(0,END)
        fname.insert(0, 'First')
        fname.config(foreground='gray')
        lname.insert(0, 'Last')
        lname.config(foreground='gray')
        rb.set(0)
        y.set(0)
        n.set(0)
        state.set('')
    except:
        #if something goes wrong, file error
        checking.set('File Error')
def first_name(event):
    #when entry is clicked, delete 'first name'
    fname.delete(0, END)
    fname.config(foreground='black')
def last_name(event):
    #when entry is clicked, delete 'last name'
    lname.delete(0, END)
    lname.config(foreground='black')
def button_status_y(*args):
    #if y is selected, don't select n
    if y.get()==1:
        n.set(0)
def button_status_n(*args):
    #if n is selected, don't select y
    if n.get()==1:
        y.set(0)
def clear(*args):
    try:
        #if there is a digit in first or last name, don't do anythin
        for i in fname.get():
            if i.isdigit():
                root.mainloop()
        for i in lname.get():
            if i.isdigit():
                root.mainloop()
        #if something is empty, don't do anything
        if y.get()==0 and n.get()==0 or rb.get()==0:
            root.mainloop()
        elif fname.get()=='' or fname.get()=='First Name' or lname.get()=='' or lname.get()=='Last Name' or state.get()=='':
            root.mainloop()
        #if it works go to write
        else:
            write(*args)
    except:
        root.mainloop()
        
root=Tk()
root.title('Entry Form')

#parent function
mainframe=ttk.Frame(root, padding='100 100 100 100')
mainframe.grid(row=1, column=1, sticky=(N,W,E,S))
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)

#string vars and int vars
First=StringVar()
Last=StringVar()
rb=IntVar()
State=StringVar()
y=IntVar()
n=IntVar()
checking=StringVar()

#first name and last name entry
fname=ttk.Entry(mainframe, textvariable=First, width=15)
fname.grid(row=1, column=1, sticky=W)
fname.insert(0, 'First Name')
fname.configure(foreground='gray')
lname=ttk.Entry(mainframe, textvariable=Last, width=15)
lname.grid(row=2, column=1, sticky=W)
lname.insert(0, 'Last Name')
lname.configure(foreground='gray')

#radiobuttons for business, residence, or other
business=ttk.Radiobutton(mainframe, text='Business', variable=rb, value=1)
business.grid(row=3, column=1, padx=10, pady=10)
residence=ttk.Radiobutton(mainframe, text='Residence', variable=rb, value=2)
residence.grid(row=3, column=2, padx=10, pady=10)
other=ttk.Radiobutton(mainframe, text='Other', variable=rb, value=3)
other.grid(row=3, column=3, padx=10, pady=10)

#states
ttk.Label(mainframe, text='State: ').grid(row=4, column=1, sticky=W)
state=ttk.Combobox(mainframe, textvariable=State, width=15, state='readonly')
state.grid(row=4, column=2, sticky=(W,E))
state['values']=('Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennesse','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming')

#checkbuttons for accept policy
ttk.Label(mainframe, text='Accept Policy?').grid(row=6, column=1, sticky=W)
yes=ttk.Checkbutton(mainframe, text='Yes', variable=y, command=button_status_y,)
yes.grid(row=6, column=2, sticky=W)
no=ttk.Checkbutton(mainframe, text='No', variable=n, command=button_status_n,)
no.grid(row=6, column=3, sticky=W)

#submit button and label
ttk.Label(mainframe, textvariable=checking).grid(row=8, column=2, sticky=W)
button=ttk.Button(mainframe, text='Submit', command=clear)
button.grid(row=7, column=3, sticky=N)

#extra padding
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=10)

#binding to enter and click
fname.bind('<Button-1>', first_name)
lname.bind('<Button-1>', last_name)
root.bind('<Return>', clear)

#do it again
root.mainloop()
