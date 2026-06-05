# l=[1,2,3,4,5,6,7,8,9]
# f=l[0]
# for i in range(0,len(l)-1):
#     l[i]=l[i+1]
# l[len(l)-1]=f
# print(l)



def rev(arr,start,end):
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp
l=[1,2,3,4,5,6]
d=3
d=d%len(l)