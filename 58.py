b=[]
for i in range(10):
    a=input("請輸入第"+str(i+1)+"個數字:")
    b.append(a)
b.sort()
print("最大3個數字:"+str(b[9])+","+str(b[8])+","+str(b[7]))
print("最小3個數字:"+str(b[2])+","+str(b[1])+","+str(b[0]))