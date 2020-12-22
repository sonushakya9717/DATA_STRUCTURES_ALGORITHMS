
######### working with stack ############

from collections import deque

class stack:
    def __init__(self):
        self.containers=deque()

    def peek(self):
        return self.containers[-1]

    def pop(self):
        return self.containers.pop()

    def push(self,val):
        self.containers.append(val)

    def show(self):
        print( self.containers)

if __name__ == "__main__":
    a=stack()
    a.push(8)
    a.show()
