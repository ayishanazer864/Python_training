l1=list(map(int,input().split()))
l1.sort()
l2=[]
for i in l1:
    if(i%2!=0):
        l2.append(i)
    else:
        l2.insert(0,i)
print(l2)
