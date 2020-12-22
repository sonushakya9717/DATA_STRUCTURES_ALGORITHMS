############## BRICK SORT ##############
a=list(map(int,input().split()))
issorted=True
while issorted==True:
    issorted=False
    for i in range(1,len(a)-1,2):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            issorted=True
    for j in range(0,len(a)-1,2):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            issorted=True
print(a)