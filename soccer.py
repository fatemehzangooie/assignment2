win=0
wqual=0
lose=0
count=1
score=0
while count<=8:
    print("write the score:  ",count,"1.win 2.equal 3.lose")
    number:int(input("result= "))
    if number == 1 :
        win+=1
        score+=3
    elif number == 2:
        equal+=1
        score+=1
    elif number == 3:
        lose+=1
        score+=0
    else:
        print("choose the option.")
        count-=1
        count+=1
        print("score: ",score,"win: ",win,"equal: ",equal,"lose: ",lose)