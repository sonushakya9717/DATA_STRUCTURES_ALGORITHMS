############# GENERAL TREE ########

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        iterator=self.parent
        while iterator:
            iterator=iterator.parent
            level+=1
        return level
    def print_tree(self):
        spaces=" "*self.get_level()*3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix,self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

if __name__ == "__main__":
    root=TreeNode('Electronics')
    Tv=TreeNode("Tv")
    phones=TreeNode("Phones")
    laptops=TreeNode("Laptops")

    Tv.add_child(TreeNode("LG"))
    Tv.add_child(TreeNode("Sony"))
    Tv.add_child(TreeNode("Sumsang"))

    phones.add_child(TreeNode("Mi"))
    phones.add_child(TreeNode("GOME"))
    phones.add_child(TreeNode("Vivo"))

    laptops.add_child(TreeNode("Lenvovo"))
    laptops.add_child(TreeNode("Apple"))
    laptops.add_child(TreeNode("Accer"))

    root.add_child(Tv)
    root.add_child(phones)
    root.add_child(laptops)

    root.print_tree()


########## BINARY TREE #############

class Binary_Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return "data is already exists"
        
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
               self.left= Binary_Tree(data)

        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
               self.right= Binary_Tree(data)
            
    def search(self,data):
        if data==self.data:
            return True
        
        if data<self.data:
            if self.left:
               return self.left.search(data)
            else:
                return False
        else:
            if self.right:
               return self.right.search(data)
            else:
                return False

    def in_order_traversal(self):
        array=[]
        if self.left:
            array+=self.left.in_order_traversal()
        array.append(self.data)
        if self.right:
            array+=self.right.in_order_traversal()
        return array


    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.data


    def sum(self):
        total=0
        if self.left:
            total+=self.left.sum()
        total+=self.data

        if self.right:
            total+=self.right.sum()

        return total

    def delete(self,data):
        if data<self.data:
            if self.left:
                self.left=self.left.delete(data)

        elif data>self.data:
            if self.right:
                self.right=self.right.delete(data)

        else:
            if self.right==None and self.left==None:
                return None
            if self.right:
                return self.right
            if self.left:
                return self.left
            else:
                max_val=self.left.max()
                self.data=max_val
                self.left=self.left.delete(max_val)
            
        return self


if __name__ == "__main__":
    a=Binary_Tree(56)
    a.add_child(45)
    a.add_child(4)
    a.add_child(5)
    a.add_child(450)
    a.add_child(8)

    print(a.search(450))
    a.delete(8)
    print(a.in_order_traversal())
    print(a.min())
    print(a.max())
    print(a.sum())
