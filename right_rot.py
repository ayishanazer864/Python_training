def rev(arr,start,end):
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
l=[1,2,3,4,6]
d=int(input("enter d:"))
d=d%len(l)
rev(l,0,len(l)-1)
rev(l,0,d-1)
rev(l,d,len(l)-1)


print(l)