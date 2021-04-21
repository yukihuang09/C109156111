m=int(input("輸入階層值:"))
n=0
a=1
while a<m:
    n+=1
    a*=n
print("超過"+str(m)+"最小階層為:"+str(n))