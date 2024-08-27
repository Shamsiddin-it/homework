def potato(a:str):
    cnt=0
    i=0
    while i<=len(a)-6:
        if a[i:i+6]=="potato":
            cnt+=1
            i+=6
        else:
            i+=1 
    print(cnt)
a=input()
potato(a)

# zadacha2
def sum_five(a):
    a=[int(i) for i in a]
    sum=0
    for i in a:
        if i>5:
            sum+=i
    print(sum)
x=input().split()
sum_five(x)



# zadacha3
def sutter(a):
    b=""
    for i in range(len(a)):
        b+=a[0]
        b+=a[1]
        break
    print(f"{b}... {b}... {a}?")
x=input()
sutter(x)



# zadacha4
def discount(a):
    for i in range(len(a)):
        m=int(a[0])-int(a[1])*int(a[0])/100
        break
    print(m)
a=input().split()
discount(a)