a=int(input("輸入"))
b=int(input("輸入"))
c=int(input("輸入"))
t=b**2-(4*a*c)
t1=0
t2=0
if t<0:
    print("0")
if t>0:
    t1=(-b+t**0.5)/(2*a)
    t2=(-b-t**0.5)/(2*a)
    print(str(t1)+","+str(t2))
elif t==0:
    t1=-b/(2*a)
    print(str(t1))
