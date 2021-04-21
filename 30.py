a=int(input("小明身上有幾元:"))
b=int(input("有幾種飲料:"))
t=0
for i in range(b):
    c=int((input("第"+str(i+1)+"種飲料:")))
    if a>=c:
        t+=1
print("可以買的飲料:"+str(t))