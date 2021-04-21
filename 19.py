a=int(input("組數"))
for i in range(a):
    b=input("第"+str(i+1)+"組:").split()
    t1=eval(b[0])*250+eval(b[1])*175
    print(str(t1))
