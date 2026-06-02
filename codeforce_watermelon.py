w=int(input())
if(w%2!=0 or w==2):
    print("No")
else:
    print("Yes")
    x=w//2
    if(x%2==0):
        print(x)
    else:
        print(x-1,x+1)