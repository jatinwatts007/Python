def funinfinding(lst,input2,item):
    n=0
    count = 0
    for value in lst:
        count=count +1
    for i in range(0,count):
        if(lst[i]==item):
            n=n+1
            print(i)
            if(input2=="1"):
                break
    if(n==0):
        print("Element is not in List")
lst = [] 
n = int(input("Enter number of elements : ")) 
   
for i in range(0, n): 
    lst = lst + [(input("Enter element no. {} : ".format(i+1)))]
item = (input("Enter element you wnat to check in list: "))
input2 = input("Press 1 to see first index and Press 1+ to see all indexes : ")
funinfinding(lst,input2,item)    
        
