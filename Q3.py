def power(x,y):
    j=1
    float(j)
    if(y==0 and x!=0):
        return 1
    if(x==0):
        return 0;
    if(y<0):
        y=-y
        for k in range(0,int(y)):
            j=j*(1/x)
    else:
        for i in range(0,int(y)):
            j=j*x
    return j
def factorial(x):
    if(x==0):
        return 1;
    k=1
    float(k)
    for i in range(2,int(x)+1):
        k=k*i
    return k;
def mode(z,x,y):
    return (z%(x+y))
def equation(power,factorial,mode):
    x=float(input("Enter of value of x: "))
    y=float(input("Enter of value of y: "))
    z=float(input("Enter of value of z: "))
    if((x==0 and y==0) or (x<0) or  x+y==0):
        return "Not defined"
    i=power(x,y)
    j=power(y,x)
    k=factorial(x)
    l=mode(z,x,y)
    print("Answer after solving equation is: ")
    return (i+j)+(k-l)
print(function(power,factorial,mode))
