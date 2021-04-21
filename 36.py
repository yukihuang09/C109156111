a=int(input("輸入:"))
t=0
while a!=1:
    print(a,end="  ")
    if a%2!=0:
        a=3*a+1
        t+=1
    else:
        a=a/2
        t+=1
print(a)
print("cycle length:"+str(t+1))