n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
d={}
for i in range(n):
    if(age[i]>18):
        if vote[i] not in d:
            d[vote[i]]=1
        else:
            d[vote[i]]+=1
k=max(d.values())
ki=max(d,key=d.get)
cnt=0
for key,val in d.items():
    if(val==k):
        cnt+=1
if cnt>1:
    print(-1)
else:
    print(ki)