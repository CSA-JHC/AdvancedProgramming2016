from tkinter import *
from tkinter import ttk
import re

def calculate(*args):
    try:
        buying=item.get()
        file=open('items.txt', 'r')
        for line in file:
            line=line.strip('\n')
            linesplit=line.split()
            if buying==linesplit[0]:
                price=re.findall('\d+', line)
                price=str(price).replace('[','').replace(']','').replace("'",'')


            
        value=int(shipping.get())
        if value==2:
            cost=int(25)
        elif value==3:
            cost=int(10)
        elif value==5:
            cost=int(5)
        num=cost+(round(cost*0.0825,2))+int(price)
        x=round(cost*0.0825, 2)
        
        total.set(num)
        tax.set(x)
    except:
        tax.set('')
        total.set('')

root=Tk()
root.title('Order Form')

mainframe=ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

item=StringVar()
shipping=StringVar()
total=StringVar()
tax=StringVar()

item_entry=ttk.Entry(mainframe, width=10, textvariable=item)
item_entry.grid(column=2, row=1, sticky=(W, E))
shipping_entry=ttk.Entry(mainframe, width=10, textvariable=shipping)
shipping_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=tax).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=total).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Order", command=calculate).grid(column=2, row=5, sticky=N)

ttk.Label(mainframe, text="Item:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Shipping (enter as a number):"+'\n'+"Two day- $25"+'\n'+"Three day- $10"+'\n'+"Five day- $5").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Tax:").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Total:").grid(column=1, row=4, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=10)

root.bind('<Return>', calculate)
