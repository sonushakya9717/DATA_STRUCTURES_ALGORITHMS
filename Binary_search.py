############## BINARY SEARCH ##############

def BINARY(L,R,elem,a):
    if L==R:
        return False
    else:
        mid=(L+R)//2
        if a[mid]==elem:
            return True
        elif elem<a[mid]:
            R=mid-1
            return BINARY(L,R,elem,a)
        else:
            L=mid+1
            return BINARY(L,R,elem,a)

element=int(input("enter the no. which you want to search :\t"))
array=[1,2,3,4,5,6,7]
L=0
R=len(array)
print(BINARY(L,R,element,array))
