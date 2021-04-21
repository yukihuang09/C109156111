a=int(input("搭了幾次電梯:"))
f=1
m=0
c=[]
for i in range(a):
    b=int(input("搭到幾樓:"))
    c.append(b)
for j in range(a):
    if f>c[j]:
        m+=(f-c[j])*20
        f=c[j]
    elif f<c[j]:
        m+=(c[j]-f)*10
        f=c[j]
print(str(m))