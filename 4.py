x=int(input("請輸入x座標:"))
y=int(input("請輸入y座標:"))
if x==0 and y==0:
    print("位於原點")
if x==0 :
    if y>0:
        print("上半平面y軸上，距離原點為根號"+str(y**2))
    elif y<0 :
        print("下半平面y軸上，距離原點為根號"+str(y**2))
if y==0:
    if x>0:
        print("右半平面x軸上，距離原點為根號"+str(x**2))
    elif x<0 :
        print("左半平面x軸上，距離原點為根號"+str(x**2))

elif (x>0 and y>0):
    print("位於第一象限，距離原點為根號"+str((x**2+y**2)))
elif (x<0 and y>0):
    print("位於第二象限，距離原點為根號"+str((x**2+y**2)))
elif (x<0 and y<0):
    print("位於第三象限，距離原點為根號"+str((x**2+y**2)))
elif (x>0 and y<0):
    print("位於第四象限，距離原點為根號"+str((x**2+y**2)))