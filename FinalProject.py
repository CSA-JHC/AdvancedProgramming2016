##MIT License
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in all
##copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##SOFTWARE.

import datetime
import time
import os

print('Welcome to the Library!'+'\n'+'INSTRUCTIONS: Whenever you see an arrow, please enter a number for what you would like to do. Whenever the words "Title" or "Author" appear, please enter the correct information. Whenever the word "Published" appears, please enter a number. Whenever the word "Genre" appears, please enter the number indicating what genre the book is.'+'\n'+'Feel free to check out books whenever you please, and be sure to check them back in. Donations are highly appreciated!' + '\n')

class Book(object):
    def __init__(self, info, file):
        self.book=info
        self.file=file
    def find(self, info, file):
        books=[]
        for line in file:
            line=line.strip('\n')
            if info in line and ' - ' not in line: #if dash not in line and genre is
                books.append(line)  #append line to list
                newline=''
                for i in line:
                    if i==',':
                        newline+=', '
                    else:
                        #decrypt
                        num=ord(i)-3
                        letter=chr(num)
                        newline+=letter
                print(newline+'\n')
        if books==[]:   #if books is empty, no current books
            print('That book is not available. ')
            time.sleep(3)
            os.system('cls')
            menu()  #menu
    
def menu():
    print('1. Check Out ')  #options
    print('2. Check In ')
    print('3. Donate ')
    try:
        choice=input('--> ')    #user puts what they want
        if choice=='1':
            os.system('cls')
            find()  #goes to find function if choice=1
        elif choice=='2':
            os.system('cls')
            checkin()   #goes to checkin function if choice=2
        elif choice=='3':
            os.system('cls')
            donate()    #goes to donate function if choice=3
        else:
            print('Not an option. ') #if user types something other than 1,2,3
            time.sleep(3)
            os.system('cls')
            menu()  #goes back to menu
    except KeyboardInterrupt:
        print("Please don't do that again! ") #if user types ctrl c
        time.sleep(3)
        os.system('cls')
        menu()  #goes back to menu

def find():
    print('Find book based on: ')   #can choose how they want to find book
    print('1. Title ')
    print('2. Author ')
    print('3. Publish Date ')
    print('4. Genre ')
    try:
        choice=input('--> ')    #input
        if choice=='1':
            os.system('cls')
            title() #goes to title function if choice=1
        elif choice=='2':
            os.system('cls')
            author()    #goes to author function if choice=2
        elif choice=='3':
            os.system('cls')
            publishdate()   #goes to publishdate function if choice=3
        elif choice=='4':
            os.system('cls')
            findgenre() #goes to genre function if choice=4
        else:
            print('Not an option. ') #if user types something other than 1,2,3,4
            time.sleep(3)
            os.system('cls')
            find()  #goes back to find function
    except KeyboardInterrupt:
        print("Please don't do that again! ") #if user types ctrl c
        time.sleep(3)
        os.system('cls')
        menu()  #goes back to menu

def donate():
    try:
        #enters info so book can be inserted into file
        print('Please enter information about the book you would like to donate below: ')
        title=input('Title: ').lower()  #enter title, lowercases it
        author=input('Author: ').lower()    #enter author, lowercases it
        pd=int(input('Published (year/four digit number): ')) #enters date
        while len(str(pd))!=4:
            os.system('cls')
            print('Please enter a four digit number. ')
            pd=int(input('Published (year/four digit number): '))
        print('1. Fiction ')
        print('2. Non-Fiction ')
        print('3. Mystery ')
        print('4. Fantasy ')
        print('5. Science Fiction ')
        print('6. Drama ')
        print('7. Romance ')
        print('8. Horror ')
        print('9. Action and Adventure ')
        print('10. Historical Fiction ')
        genre=input('Genre: ').lower()  #enters genre, lowercases it
        if genre=='1':
             genre='fiction'
        elif genre=='2':
            genre='nonficton'
        elif genre=='3':
            genre='mystery'
        elif genre=='4':
            genre='fantasy'
        elif genre=='5':
            genre='science fiction'
        elif genre=='6':
            genre='drama'
        elif genre=='7':
            genre='romance'
        elif genre=='8':
            genre='horror'
        elif genre=='9':
            genre='action and adventure'
        elif genre=='10':
            genre='historical fiction'
        else:
            os.system('cls')
            print("That wasn't an option! Please try again. ")
            genre()

        #encryption
        newt=''
        for i in title:
            num=ord(i)+3
            letter=chr(num)
            newt+=letter 
        newa=''
        for i in author:
            num=ord(i)+3    
            letter=chr(num)
            newa+=letter 
        newpd=''
        for i in str(pd):
            num=ord(i)+3
            letter=chr(num)
            newpd+=letter
        newg=''
        for i in genre:
            num=ord(i)+3
            letter=chr(num)
            newg+=letter
    except:
        print('You entered something wrong. ')   #something didn't work
        time.sleep(3)
        os.system('cls')
        donate()

    try:
        #print info
        os.system('cls')
        print('--------------------')
        print('Title: '+title)
        print('Author: '+author)
        print('Published: '+str(pd))
        print('Genre: '+genre)
        print('--------------------')
        choice=input('Is all this information correct (yes or no)? ').lower()
        if choice=='no':
            os.system('cls')
            donate()
    except:
        print('You entered something wrong. ')
        time.sleep(3)
        os.system('cls')
        donate()
    try:
        file=open('INVENTORY.txt','a')  #open files
        file.write(newt+', '+newa+', '+newpd+', '+newg+'\n')   #writes info into file
        file.close()    #closes file
        os.system('cls')
        print('Thanks for the donation! ')  #thanks for donation
        time.sleep(3)
        os.system('cls')
        menu()  #goes to menu
    except:
        print('File Error. ')
        time.sleep(3)
        os.system('cls')
        menu()

def title():
    try:
        title=input('What is the title? ').lower()  #find book based on title
        newt=''
        #encrypt
        for i in title:
            num=ord(i)+3
            letter=chr(num)
            newt+=letter
    except KeyboardInterrupt:
        print("Please don't do that again! ")
        time.sleep(3)
        os.system('cls')
        menu()
    try:
        file=open('INVENTORY.txt','r')  #open file
        #goes to class
        stuff=Book(title, file)
        stuff.find(newt, file)
        file.close()    #close file
    except:
        print("File Error. ")    #uh oh.. something happened
        time.sleep(3)
        os.system('cls')
        menu()

    checkout()  #goes to checkout function

def author():
    try:
        author=input('Who is the author? ').lower() #find book based on author
        newa=''
        #encrypt
        for i in author:
            num=ord(i)+3
            letter=chr(num)
            newa+=letter
    except KeyboardInterrupt:
        print("Please don't do that again! ")
        time.sleep(3)
        os.system('cls')
        menu()
        
    try:
        file=open('INVENTORY.txt','r')  #open file
        stuff=Book(title, file)
        stuff.find(newa, file)
        file.close()    #close file
    except:
        print('File Error. ')    #file doesn't work
        time.sleep(3)
        os.system('cls')
        menu()
    
    checkout()  #goes to checkout function

def publishdate():
    try:
        pd=int(input('What time period? '))  #find book based on date published
        newpd=''
        #encrypt
        for i in str(pd):
            num=ord(i)+3
            letter=chr(num)
            newpd+=letter
    except:
        print("That isn't a number. ")   #didn't enter number
        time.sleep(3)
        os.system('cls')
        publishdate()
        
    try:        
        file=open('INVENTORY.txt')  #open file
        stuff=Book(title, file)
        stuff.find(newpd, file)
        file.close()    #close file
    except:
        print('File Error. ')    #file error
        time.sleep(3)
        os.system('cls')
        menu()
    checkout()  #goes to checkout function

def findgenre():
    try:
        print('1. Fiction ')
        print('2. Non-Fiction ')
        print('3. Mystery ')
        print('4. Fantasy ')
        print('5. Science Fiction ')
        print('6. Drama ')
        print('7. Romance ')
        print('8. Horror ')
        print('9. Action and Adventure ')
        print('10. Historical Fiction ')
        genre=input('What genre? ').lower() #find book based on genre
        if genre=='1':
            genre='fiction'
        elif genre=='2':
            genre='nonficton'
        elif genre=='3':
            genre='mystery'
        elif genre=='4':
            genre='fantasy'
        elif genre=='5':
            genre='science fiction'
        elif genre=='6':
            genre='drama'
        elif genre=='7':
            genre='romance'
        elif genre=='8':
            genre='horror'
        elif genre=='9':
            genre='action and adventure'
        elif genre=='10':
            genre='historical fiction'
        else:
            os.system('cls')
            print("That wasn't an option! Please try again. ")
            findgenre()
        newg=''
        #encrypt
        for i in genre:
            num=ord(i)+3
            letter=chr(num)
            newg+=letter
    except KeyboardInterrupt:
        print("Please don't do that again! ")
        time.sleep(3)
        os.system('cls')
        menu()

    try:
        file=open('INVENTORY.txt','r')  #open file
        stuff=Book(title, file)
        stuff.find(newg, file)
        file.close()    #close file

    except:
        print('File Error. ')
        time.sleep(3)
        os.system('cls')
        menu()
    checkout()  #goes to checkout function
    
def checkout():
    taking=[]   #list
    try:
        ask=input('Check out a book (yes or no)? ').lower() #checkout a book??
        if ask=='no':   #if no then go to menu
            os.system('cls')
            menu()
        elif ask=='yes':    #if yes
            print('What book would you like to check out? ')    #which book
            title=input('Title: ')  #enter title
            author=input('Author: ')    #enter author
            pd=int(input('Published: '))
            x=False

            #encryption
            newpd=''
            for i in str(pd):
                num=ord(i)+3
                letter=chr(num)
                newpd+=letter
            newt=''
            for i in title:
                num=ord(i)+3
                letter=chr(num)
                newt+=letter
            newa=''
            for i in author:
                num=ord(i)+3
                letter=chr(num)
                newa+=letter

            try:
                file=open('INVENTORY.txt', 'r')  #open file
                for line in file:
                    if newt+', '+newa+', '+newpd in line:   #if title and author in line
                        x=True  #x is true
                file.close()
                
                if x==True: #if x is true
                    name=input('What is your name? ').lower()   #enter name
                    while name=='':
                        print("Please enter your name. ")
                        name=input('What is your name? ')
                    file=open('INVENTORY.txt', 'r')
                    for line in file:
                        line=line.strip('\n')   #strip new line in line
                        if newt+', '+newa+', '+newpd in line:   #if title and author in line
                            taking.append(line+' - '+str(datetime.datetime.now())+', '+name) #append line and date and name to list
                        elif newt+', '+newa+', '+newpd not in line: #if title and author not in line
                            taking.append(line) #append line to list
                    file.close() #close file
                    write_out(taking)
                elif x==False:  #if x is still false
                    print('That book is not available. ')  #book is not available
                    time.sleep(3)
                    os.system('cls')
                    menu()
                    
            except:
                print('File Error. ')
                time.sleep(3)
                os.system('cls')
                checkout() 
        else:
            print('Not an option. ')
            time.sleep(3)
            os.system('cls')
            checkout()

    except KeyboardInterrupt:   #if user types ctrl c
        print('Not an option. ')
        time.sleep(3)
        os.system('cls')
        checkout()  #goes to checkout function

def write_out(books):
    try:
        file=open('INVENTORY.txt','w')
        for i in books:
            file.write(i+'\n')
        file.close()
        os.system('cls')
        print('Checkout Successful! ')   #yay, checkout works
        time.sleep(3)
        os.system('cls')
        menu()  #goes back to menu
    except:
        print('File Error. ')    #if file doesn't work
        time.sleep(3)
        os.system('cls')
        checkout()  #go to checkout

def checkin():
    try:
        title=input('Title: ').lower()
        author=input('Author: ').lower()
        pd=int(input('Published: '))
        name=input('Name: ').lower()
    except:
        print("You entered something wrong. ")
        time.sleep(3)
        os.system('cls')
        checkin()

    #encryption
    newt=''
    for i in title:
        num=ord(i)+3
        letter=chr(num)
        newt+=letter
    newa=''
    for i in author:
        num=ord(i)+3
        letter=chr(num)
        newa+=letter
    newpd=''
    for i in str(pd):
        num=ord(i)+3
        letter=chr(num)
        newpd+=letter
    try:
        books=[]
        file=open('INVENTORY.txt','r+')  #opens file
        for line in file:
            line=line.strip('\n')
            if newt+', '+newa+', '+newpd and ' - ' and name in line: #if info in file
                books.append(line)  #add line to books
        file.close()    #closes file
        if books==[]:   #book is empty
            print('That book is not in our inventory. ') #not in inventory
            time.sleep(3)
            os.system('cls')
            menu()
        elif books!=[]: #if book in list
            write_in(books, newt, newa) #go to write function
    except:
        print('File Error. ')    #file doesn't work
        time.sleep(3)
        os.system('cls')
        menu()

def write_in(check, n, a):
    try:
        rewrite=[]
        for i in check: #for i in list
            if ' - ' and n and a in i:  #if info in line/i of list
                rewrite.append(i)   #append to rewrite
        if rewrite==[]: #if rewrite is empty
            print('There is no such book. ')
            time.sleep(3)
            os.system('cls')
            menu()
        else:
            checkin=[]
            space=0
            newline=''
            for x in i: #for x in line/i of list
                if x==' ':  #if x is a dash
                    space+=1
                elif space==4:
                    checkin.append(newline) #append newline to list
                    break
                elif x==',':
                    newline+=', '
                elif x!='-':    #if x is not dash
                    newline+=x  #add to newline
        file=open('INVENTORY.txt','r')  #read file
        for line in file:
            line=line.strip('\n')
            if ' - ' not in line:   #if dash not in line
                checkin.append(line)    #add to list
            elif n and a not in line:   #if name and author not in line
                checkin.append(line)    #add list
        file.close()

        file=open('INVENTORY.txt', 'w') #write to file
        for i in checkin:   #for every book in list
            file.write(i+'\n')  #write to file with newline
        file.close()
        os.system('cls')
        print('Checkin Successful! ')
        time.sleep(3)
        os.system('cls')
        menu()
    except:
        print('File Error') #file doesn't work
        time.sleep(3)
        os.system('cls')
        checkin()
menu()
