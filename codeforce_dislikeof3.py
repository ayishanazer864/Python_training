t=int(input())
a=[]
n=1
while(len(a)<1000):
    if(n%3!=0 and n%10!=3):
        a.append(n)
    n=n+1
for i in range(t):
    k=int(input())
for i in k:
    print(a[k - 1])