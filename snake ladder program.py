import random
count=0
while(count<=100):
    n=input("press to roll a dice")
    if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("your random is",r)
        print("your count is",count)
        if count==8:
            count=37
            print("ohh you climb the ladder and count is",count)
        if count==13:
            count=34
            print("ohh you climb the ladder and count is",count)
        if count==40:
            count=68
            print("ohh you climb the ladder and count is",count)
        if count==52:
            count=81
            print("ohh you clim the ladder and count is",count)
        if count==76:
            count=97
            print("ohh you climb the ladder and count is",count)
        if count==11:
            count=25 
            print("snake bit count is",count)
        if count==25:
             count=4
             print("snake bit count is",count)
        elif count==38:
             count=9
             print("snake bit count is",count)
        elif count==65:
              count=46
              print("snake bit count is",count)
        elif count==89:
              count=70
              print("snake bit count is",count)
        elif count==97:
               count=76
               print("snake bit count is",count)
        elif count>=100:
               print("win")
        else:
            print("continue the game")
            
        
            
