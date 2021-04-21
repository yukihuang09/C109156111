while True:
    a=list(input("輸入字串(end結束):"))
    if a[0]=="e"and a[1]=="n" and a[2]=="d":
        print("檢測結束")
        break
    else:b=input("檢測字元:")
    print(a.count(b))
