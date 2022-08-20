even=0
odd=0
x=int(input("write your number: "))
while (x)!=0 :
     a =(x%10)
if ((a%2)==0) or (a==0):
    even+=1
else:
    odd+=1
    x=x//10
    print("the number of odd number:" , odd , 'the number of even number:' , even)
    if(odd>even):
        print("the odd number is more")
    elif(odd==even):
        print("yhe number of odd number is equal to the number of even number")
        
    else:
            print("the even number is more")
    