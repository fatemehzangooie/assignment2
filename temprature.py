while True:
    dama=float(input('write your temperature:'))
    temp1=input("write your first temprature: celsius..C / farenhite..F / kelvin..K")
    temp2=input("write your seconed temprature: celsius..C / farenhite..F / kelvin..K")
    if temp1=='C' and temp2 =="F":
        F = (dama*1.8)+32
        print("farenhite=",F)
        
    elif temp1 =='F' and temp2 == 'C':
        C = (dama - 32)/1.8 
        print('celsius=',C)
        
    elif temp1 == 'K' and temp2 == 'C':
        C = dama - 273.15
        print('celsius=', C)
        
    elif temp1 == 'C' and temp2 == 'K':
        K=dama + 273.15
        print("kelvin=", K)
        
    elif temp1 == 'F' and temp2 == 'K':
        print('kelvin=', (dama + 459.67)/1.8)
        
    elif temp1 == 'K' and temp2 == "F":
        print('farenhite=',(dama*1.8)-459.67)
        
    else:
        print("try again!")            
    