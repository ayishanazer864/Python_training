l=[2,3,1,5,2,4,6,7,8,5,2,2,3]
k=3
s=l[0]+l[1]+l[2]
max=s
for i in range(1,len(l)-k+1 ):
    s=s-l[i-1]+l[i+k-1]
    if(s>max):
        max=s
        strt=i
print(strt,strt+1,strt+2)