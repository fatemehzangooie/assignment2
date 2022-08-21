username=("fatemeh zangooie")
password=("99154223")
w=0
while w<=2:
    a=input("write your username:")
    b=input("write your password:")
    if(a=="fatemeh zangooie" and b=="99154223"):
        print("done")
        break
    else:
        print("wrong .. please check")
        w = w + 1
        if (w>2):
            print("it is not possible to access")