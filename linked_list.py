
################## Linked List ####################

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    

class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        if self.head==None:
            elements=Node(data,None)
            self.head=elements
        else:
            elements=Node(data,self.head)
            self.head=elements
    def printll(self):
        if self.head==None:
            print("linked is empty")
            return
        iterator=self.head
        llstr=""
        while iterator:
            llstr+=str(iterator.data)+"-->" if iterator.next else str(iterator.data)
            iterator=iterator.next
        print(llstr)
    
    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(data,None)
            return
        iterator=self.head
        while iterator.next:
            iterator=iterator.next
        iterator.next=Node(data,None)
    def get_length(self):
        count=0
        iterator=self.head
        while iterator:
            count+=1
            iterator=iterator.next
        return count
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("index out of range")
        count=0
        iterator=self.head
        while iterator:
            if count==index-1:
                element=Node(data,iterator.next)
                iterator.next=element
                break
            iterator=iterator.next
            count+=1

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("index out of range")
        count=0
        iterator=self.head
        if index==0:
            self.head=iterator.next
            return
        while iterator:
            if count==index-1:
                iterator.next=iterator.next.next
                break
            iterator=iterator.next
    def insert_value(self,li):
        for i in li:
            self.insert_at_end(i)
    
    def inser_afterdata(self,data_after,data_to_insert):
        iterator=self.head
        while iterator:
            if iterator.data==data_after:
                element=Node(data_to_insert,iterator.next)
                iterator.next=element
                return
            iterator=iterator.next
        raise Exception("There is no data")

    def remove_by_value(self,data):
        iterator=self.head
        if iterator.data==data:
            self.head=iterator.next
            return
        while iterator:
            if iterator.next.data==data:
                iterator.next=iterator.next.next
                return
            iterator=iterator.next
        raise Exception("there is no data")


if __name__ == "__main__":
    a=linkedlist()
    a.insert_at_begining(23)
    a.insert_at_begining(23)
    a.insert_at_begining(23)
    a.insert_at_begining(245)
    a.printll()
    print(a.get_length())
    a.insert_at_end(45)
    a.insert_at(3,500)
    a.remove_at(0)
    a.insert_value([2,3,4,5,6,7])
    a.inser_afterdata(7,67)
    a.remove_by_value(67)
    a.printll()
