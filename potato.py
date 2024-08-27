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