import time

print('PROGRAM ONE:')
import random
nums=[]
for i in range(10):
    x=random.randrange(1, 50)
    while x in nums:
        x=random.randrange(1,50)
    nums.append(x)
    print(x)

    
print('\n'+"PROGRAM TWO:")
def questions():
    class Car(object):
        def __init__(self,c,y,t):
            self.c=c
            self.y=y
            self.t=t
        def ask(self):
            return 'You have a '+c+' car from '+str(y)+' that can go '+str(t)+' miles per hour.'
    try:
        c=input("What color is the car? ")
        y=int(input("What year is the car? "))
        t=int(input("What is the car's top speed? "))
        x=Car(c,y,t)
        print(x.ask())
    except ValueError:
        print('You typed something incorrectly.. ')
        questions()
questions()

