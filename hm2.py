# import random
# a=random.randint(1,100)
# i=1
# cnt=0
# while i<=5:
#     b=int(input())
#     i+=1
#     if a-b==0:
#         print("You win!!!")
#         break
#     elif abs(a-b)<=5:
#         print("You are too close")
#         cnt+=1
#         continue
#     elif abs(a-b)>5 and abs(a-b)<=20:
#         print("close")
#         cnt+=1
#         continue
#     elif abs(a-b)>20 and abs(a-b)<=30:
#         print("far")
#         cnt+=1
#         continue
#     else:
#         print("too far")
#         cnt+=1
#         continue
# if cnt==5:
#     print("Game over") 
#     print("the number was", a)   

# 3
# import random
# a=int(input())
# b="qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*"
# new=random.choices(b, k=a)
# m=""
# for i in new:
#     m+=i
# print(m)    

# 4
# import random
# a=["rock","paper","scissors"]
# b=random.choice(a)
# c=int(input("1-rock,2-paper,3-scissors: "))
# if c==1:
#     if b=="rock":
#         print("Computer choose rock. It's a tie!")
#     elif b=="paper":
#         print("Computer choose paper. You lose!")
#     elif b=="scissors":
#         print("Computer choose scissors. You win!")
# elif c==2:
#     if b=="rock":
#         print("Computer choose rock. You win!")
#     elif b=="paper":
#         print("Computer choose paper. Its a tie!")
#     elif b=="scissors":
#         print("Computer choose scissors. You lose!")
# elif c==3:
#     if b=="rock":
#         print("Computer choose rock. You lose!")
#     elif b=="paper":
#         print("Computer choose paper. You win!")
#     elif b=="scissors":
#         print("Computer choose scissors. Its a tie!")

