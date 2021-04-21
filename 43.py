a=int(input("輸入班級數:"))
c=[]
for i in range(a):
    b=int(input("人數:"))
    c.append(b)
    c.sort()
print("需要買"+str(c[a-1]))
