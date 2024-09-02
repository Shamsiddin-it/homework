# a=input()
# for i in range(len(a)):
#     print(a[i]*2,end="")

# 2
# def note(a):
#     with open("notes.txt", 'r') as file:
#         new = file.readlines()
#         cnt=0
#         for i in new:
#             i=str(i).split()
#             for j in i:
#                 if j==a:
#                     cnt+=1
#         print(cnt)
# a=input()
# note(a)

# 3
# def note(a):
#     with open("notes.txt", 'r') as file:
#         new = file.readlines()
#         cnt=0
#         for i in new:
#             i=str(i).split()
#             for j in i:
#                 if j.endswith(a):
#                     cnt+=1
#         print(cnt)
# a=input()
# note(a)

# 4
# def note():
#     with open("notes.txt", 'r') as file:
#         new = file.readlines()
#         cnt=0
#         for i in new:
#             i=str(i).split()
#             for j in i:
#                 if j=="this" or j=="theese":
#                     cnt+=1
#         print(cnt)
# note()


# 5
# def googlify(a):
#     m='o'
#     if a>=2:
#         print(f"G{m*a}gle")
#     else:
#         print("invalid")
# a=int(input())
# googlify(a) 


# 6
# a=[i for i in input().split(',')]
# m=input()
# cnt=0
# for i in a:
#     i=str(i)
#     if m in i:
#         cnt+=1
# print(cnt>0)

# 7
# def coffe(a):
#     print(a//6+a)
# a=int(input())
# coffe(a)


# 8
# def first_last(a):
#     for i in range(len(a)):
#         print(a[0]+a[-1])
#         break
# a=input()
# first_last(a)


# 9
# def plural(a):
#     a=str(a)
#     print(a.endswith('s'))
# a=input()
# plural(a)
