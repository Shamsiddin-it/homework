import random
a=random.randint(1,100)
i=1
cnt=0
while i<=5:
    b=int(input())
    i+=1
    if a-b==0:
        print("You win!!!")
        break
    elif abs(a-b)<=5:
        print("You are too close")
        cnt+=1
        continue
    elif abs(a-b)>5 and abs(a-b)<=20:
        print("close")
        cnt+=1
        continue
    elif abs(a-b)>20 and abs(a-b)<=30:
        print("far")
        cnt+=1
        continue
    else:
        print("too far")
        cnt+=1
        continue
if cnt==5:
    print("Game over") 
    print("the number was", a)   
