l=[1,2,2,3,4,1,2,2]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
max=0
max2=0
e2=0
e1=0
for i in d:
    if(d[i]>max):
        max2=max
        e2=e1
        max=d[i]
        e1=i
    elif max2<d[i] and max2!=max:
        max2=d[i]
        e2=i
print(e2)