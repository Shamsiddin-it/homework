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


# zadacha5
def end_corona(a):
    for i in range(len(a)):
        m=int(a[2])
        n=(int(a[0])-int(a[1]))
        break
    if m%n==0:
        x=m//n
    else:
        x=m//n+1
    print(x)
a=input().split()
end_corona(a)


# zadacha6
def split(a:int):
    m=a//2
    n=a-m
    new=[]
    new.append(m)
    new.append(n)
    print(new)
a=int(input())
split(a)


# zadacha7
def twolists(a):
    for i in range(len(a)):
        print(a[0]==a[1])
        break
a=[list(i) for i in input().split(",")]
twolists(a)

# zadacha8
def new_word(a):
    for i in range(len(a)):
        print(a[1:])
        break
a=input()
new_word(a)
    

# zadacha9
def harmonic(a:int):
    n=1
    sum=0
    while n<=a:
        sum+=1/n
        n+=1
    print(sum)
a=int(input())
harmonic(a)

# zadacha10
def rev(a):
    new=""
    for i in a:
        i=str(i)
        if i.isupper():
            b=i.lower()
            new+=b
        else:
            b=i.upper()
            new+=b
    print(new[::-1])
a=input()
rev(a)
