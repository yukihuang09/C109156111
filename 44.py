m=int(input("月:"))
d=int(input("日:"))
s=0
s=(m*2+d)%3
if s==0:
    print("普通")
if s==1:
    print("吉")
if s==2:
    print("大吉")