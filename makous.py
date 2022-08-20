while True:
    a=0
    b=x=int(input("write the number: "))
    if(x>0):
        while ((x)!=0):
            n=(x%10)
            a=(a*10)+n
            x=(x//10)
            print(b)
            print(a)
            if(a==b):
                print("ada ba makous barabar ast")
            else:
                print("adad ba makous barabar nist!")
    else:
                print("adad manfi ast!")