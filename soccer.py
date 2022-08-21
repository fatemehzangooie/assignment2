win=0
equal=0
lose=0
count=1
score=0
point=0
while count<=8:
    print("write the score:  ",count,"1.win 2.equal 3.lose")
    point=int(input('your point: '))
    print('----------')
    if point == 3 :
        win+=1
        score+=1
        count==1
    elif point == 0:
        lose+=1
        score+=0
        count==1
    elif point == 1:
        equal+=1
        score+=1
        count+=1
    else:
        print("try again.")
        count-=1
        count+=1
        print("score: ",score,"win: ",win,"equal: ",equal,"lose: ",lose)