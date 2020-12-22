
class HashTable:
    def __init__(self):
        self.Max=100
        self.arr=[None for i in range(self.Max)]
    
    def get_hash(self,key):
        h=0
        for char in str(key):
            h+=ord(char)
        return h%self.Max
    
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val



    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]

# a=HashTable()
# print(a.get_hash('A'))
# a['key']=68
# print(a['key'])

#################### HASH TABLE WITH COLLISION HANDLING ####################

class new_Hash_Table:
    def __init__(self):
        self.Max=50
        self.arr=[[] for i in range(self.Max)]
    
    def get_hash(self,key):
        h=0
        for char in str(key):
            h+=ord(char)
        return h%self.Max
    
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found=False
        for ind, elements in enumerate(self.arr[h]):
            if len(elements)==2 and elements[0]==key:
                self.arr[h][ind]=(key,val)
                found=True
        if not found:
            self.arr[h].append((key,val))



    def __getitem__(self,key):
        h=self.get_hash(key)
        for pair in self.arr[h]:
            if pair[0]==key:
                return pair[1]

    def printli(self):
        print(self.arr)

# a=new_Hash_Table()
# a.__setitem__('march 6',7880)
# a.__setitem__('march 17',45)
# a.__getitem__('march 17')
# print(a.get_hash('march 6'))
# print(a.get_hash('march 17'))
# a.printli()
