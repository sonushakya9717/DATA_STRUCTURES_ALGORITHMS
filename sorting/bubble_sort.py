
############ BUBBLE SORT ###############
a= list(map(int, input("Enter a multiple value: ").split()))
stop=True
for i in range(len(a)):
    if stop==False:
        break
    stop=False
    for j in range(len(a)-(i+1)):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            stop=True
print(a)