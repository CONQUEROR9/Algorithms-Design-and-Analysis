# how do we start here
# create a class called Node
class Node(object):  # object is the primitive class, so I inherit
    # left``
    # right
    # key
    # when you first create the Node, this guy is the root node
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key  # this is actually the root node
        # why you don't write like this
        # self.root = key

    # def insert
    def insert(self, key):
        # if we already have a root node,
        if (self.key):
            # then check left and right
            # cond1:  if less than: go left
            if (key < self.key):
                # cond1.1  if the left is NIL, yay! fill it!
                if (self.left == None):
                    self.left = Node(key)
                # cond1.2  if the left is NOT NIL...oh no...
                else:
                    self.left.insert(key)

            # cond2:  if greater than: go right
            elif (key >= self.key):
                # cond1.2  if the right is NIL, yay! fill it!
                if (self.right == None):
                    self.right = Node(key)
                # cond1.2  if the right is NOT NIL...consider right as the parent...
                else:
                    self.right.insert(key)


        # if we don't have the root node
        else:
            # this key is the root node
            self.key = key

    # def printTree
    def printT(self):
        # if left is still available print left
        if (self.left):
            self.left.printT()
        print(self.key)
        if (self.right):
            self.right.printT()

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    # def delete
    def deleteT(self, key):
        if key.left == None:
            self.transplant(key, key.right)
        elif key.right == None:
            self.transplant(key, key.left)
        else:
            y = self.Tree_Minimum(key.right)
            if y.parent != key:
                self.transplant(y, y.right)
                y.right = key.right
                y.right.parent = y
            self.transplant(key, y)
            y.left = key.left
            y.left.parent = y

    # def minimum
    def Tree_Minimum(x):
        while x.left != None:
            x = x.left
        return x

    # def successor
    def Tree_Successor(self,x):
        if x.right != None:
            return self.Tree_Minimum(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y


# try our class

root = Node(103)
root.insert(11)
root.insert(51)
root.insert(44)
root.insert(333)
root.insert(35)
root.insert(34)
root.insert(10)
root.insert(13)
root.insert(32)
root.printT()
