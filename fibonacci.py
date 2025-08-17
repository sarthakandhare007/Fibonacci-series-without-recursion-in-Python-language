r=int(input("Enter a Range:"))
a=-1
b=1
for i in range(0,r):
    c=a+b
    print(f"{c}", end=" ")
    a=b
    b=c
    
