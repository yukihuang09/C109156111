a=int(input("可能有幾個點:"))
t=0
t1=0
c=[]
for i in range(a):
    b=input("第"+str(i+1)+"個點:")
    c.append(b)
for j in range(a):
    if (eval(c[j])%9==0 or eval(c[j])==0):
        print("有可能是第"+str(j+1)+"個點:"+c[j])
