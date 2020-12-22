
################## working with queue ###################

class queue:
    def __init__(self):
        self.containers=deque()

    def peek(self):
        return self.containers[-1]

    def pop(self):
        return self.containers.pop()

    def push(self,val):
        self.containers.appendleft(val)
    
    def is_empty(self):
        return len(self.containers)==0
    
    def length(self):
        return len(self.containers)
    def show(self):
        print(self.containers)

if __name__ == "__main__":
    a=queue()
    a.push(5)
    a.push(9)
    print(a.is_empty())
    print(a.length())
    a.show()
