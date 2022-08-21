number=int(input("please enter the number: "))
number1=number
reverse=0
while(number>0):
    mod=number%10
    reverse=(reverse*10)+mod
    number=number//10
    
    if number1==reverse:
        print("it is correct.")
    else:
        print('your number',number1,'and its reverse',reverse,'are not correct.')
