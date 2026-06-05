    n=int(input())
    l=list(map(int,input().split()))
    count=0
    police=0
    for i in l:
        if(i==-1):
            if police>0:
                police=police-1
            else:
                count+=1
        else:
            police+=e
    print(count)

