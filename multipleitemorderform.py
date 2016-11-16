from tkinter import *
from tkinter import ttk
import re

def calculate(*args):
    #find cost of everything
    try:
        buying=[item1.get(), item2.get(), item3.get(), item4.get()]                 #all items
        totalcost=[amount1.get(), amount2.get(), amount3.get(), amount4.get()]      #all amounts
        finalcost=0     #starting cost
        for i in range(len(buying)):
            buying[i]=buying[i].lower().replace(' ','')
            file=open('items.txt', 'r') #open file
            for line in file:
                line=line.strip('\n')
                linesplit=line.split()
                if buying[i]==linesplit[0]:
                    #find price
                    price=re.findall('\d+', line)
                    price=str(price).replace('[','').replace(']','').replace("'",'')
                    #mulitply price by amount and add to total
                    totalprice=int(price)*int(totalcost[i])
                    finalcost+=totalprice

        #ship cost
        value=int(shipping.get())
        if value==2:
            shipcost=int(25)
        elif value==3:
            shipcost=int(10)
        elif value==5:
            shipcost=int(5)
        #find tax and total cost
        taxcost=round(((finalcost+shipcost)*0.0825),2)
        cost=taxcost+finalcost+shipcost
        #set values
        total.set(cost)
        tax.set(taxcost)

    except:
        #if something goes wrong, set tax and total to nothing
        tax.set('')
        total.set('')

root=Tk()
root.title('Order Form')

#size of frame
mainframe=ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#variables
item1=StringVar()
item2=StringVar()
item3=StringVar()
item4=StringVar()
amount1=StringVar()
amount2=StringVar()
amount3=StringVar()
amount4=StringVar()
shipping=StringVar()
total=StringVar()
tax=StringVar()

#item entries
item_entry1=ttk.Entry(mainframe, width=10, textvariable=item1)
item_entry1.grid(column=2, row=1, sticky=(W, E))
item_entry2=ttk.Entry(mainframe, width=10, textvariable=item2)
item_entry2.grid(column=2, row=2, sticky=(W, E))
item_entry3=ttk.Entry(mainframe, width=10, textvariable=item3)
item_entry3.grid(column=2, row=3, sticky=(W, E))
item_entry4=ttk.Entry(mainframe, width=10, textvariable=item4)
item_entry4.grid(column=2, row=4, sticky=(W, E))

#amount entries
amount_entry1=ttk.Entry(mainframe, width=5, textvariable=amount1)
amount_entry1.grid(column=4, row=1, sticky=(W, E))
amount_entry2=ttk.Entry(mainframe, width=5, textvariable=amount2)
amount_entry2.grid(column=4, row=2, sticky=(W, E))
amount_entry3=ttk.Entry(mainframe, width=5, textvariable=amount3)
amount_entry3.grid(column=4, row=3, sticky=(W, E))
amount_entry4=ttk.Entry(mainframe, width=5, textvariable=amount4)
amount_entry4.grid(column=4, row=4, sticky=(W, E))

#shipping entries
shipping_entry=ttk.Entry(mainframe, width=10, textvariable=shipping)
shipping_entry.grid(column=2, row=5, sticky=(W, E))

#tax and total label and button
ttk.Label(mainframe, textvariable=tax).grid(column=2, row=6, sticky=(W, E))
ttk.Label(mainframe, textvariable=total).grid(column=2, row=7, sticky=(W, E))
ttk.Button(mainframe, text="Order", command=calculate).grid(column=2, row=8, sticky=N)

#text labels
ttk.Label(mainframe, text="Item(s):").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Amount:").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Shipping (enter as a number):"+'\n'+"Two day- $25"+'\n'+"Three day- $10"+'\n'+"Five day- $5").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Tax:").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Total:").grid(column=1, row=7, sticky=W)

#format
for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=10)

#enter is connected to enter key
root.bind('<Return>', calculate)

#start on entry 1
item_entry1.focus()

#do it again
root.mainloop()
