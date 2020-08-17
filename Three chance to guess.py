import random
a=0;
n=random.randint(1,11)
print(n)
while(True):
    if(a<3):
        m=int(input("Enter Number between 1-10: "))
        if(m==n):
            print("you are right")
            a=4;
        else:
            print("Try again")
        a=a+1
    if(a==3):
        print("you have lost all your chances")
    if(a==5 or a==3):
        i=input("Do you want to play again yes or no: ")
        if(i=="yes"):
            a=0
            n=random.randint(1,11)
            print(n)
        else:
            break
        
    
