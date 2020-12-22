############ Insertion Sort ################

a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[j]<a[j-1]:
            a[j-1],a[j]=a[j],a[j-1]
print(a)
