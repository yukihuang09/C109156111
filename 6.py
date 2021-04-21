a=list(input("輸入"))
b= int("".join(sorted(a)))
c= int("".join(sorted(a,reverse=True)))
print(str(c-b))