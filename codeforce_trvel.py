n,m,a,b=map(int,input().split())
cost=0
if a*m<b:
    print(a*n)
else:
    while(n>m):
        cost=cost+b
        n=n-m
    cost=cost+(n*a)
    print(cost)