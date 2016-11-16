def calculate(*args):
    try:
        buying=[item1.get(), item2.get()]
        totalcost=[amount1.get(), amount2.get()]
        file=open('items.txt', 'r')
        for line in file:
            line=line.strip('\n')
            linesplit=line.split()
            if x==linesplit[0]:
                price=re.findall('\d+', line)
                price=str(price).replace('[','').replace(']','').replace("'",'')


            
        value=int(shipping.get())
        if value==2:
            cost=int(25)
        elif value==3:
            cost=int(10)
        elif value==5:
            cost=int(5)
        num=cost+(round(cost*0.0825,2))+int(price*int(amount1.get()))
        x=round(cost*0.0825, 2)
        
        total.set(num)
        tax.set(x)
    except:
        tax.set('')
        total.set('')
