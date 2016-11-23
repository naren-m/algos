"""
    Binary Search Tree
    ------------------
    BST is a collection of nodes arranged in a way where they maintain BST
    properties. Each node has a key and an associated value. While searching,
    the desired key is compared to the keys in BST and if found, the
    associated value is retrieved.

    Link: https://www.tutorialspoint.com/data_structures_algorithms/binary_search_tree.htm
"""
class BinarySearchTree:
    """
        Implementation of Binary Search Tree
    """
    def __init__(self, data = None):
        self.data = data
        self.root = self
        self.left = None
        self.right = None
        self.parentNode = None

    def isEmpty(self):
        return  self.root.data == None

    def insert(self, data):
        """
            Insert element to BST
        """
        if self.isEmpty():
            self.root = BinarySearchTree(data)
            return

        if self.data < data:
            if self.right == None:
                self.right = BinarySearchTree(data)
                self.right.parentNode = self
            else:
                self.right.insert(data)
        else :
            if self.left == None:
                self.left = BinarySearchTree(data)
                self.left.parentNode = self

            else:
                self.left.insert(data)

    def find(self, data):
        """
            Finding element in BST
        """
        if self.data == data :
            return True
        elif self.data > data:
            if self.left == None:
                return False
            else:
                return self.left.find(data)
        else :
            if self.right == None:
                return False
            else:
                return self.right.find(data)

    def inOrder(self):
        """
           InOrder tree traversal
        """
        if self.left != None:
            self.left.inOrder()
        print self.data
        if self.right != None:
            self.right.inOrder()

    def preOrder(self):
        """
           PreOrder tree traversal
        """
        print self.data
        if self.left != None:
            self.left.preOrder()
        if self.right != None:
            self.right.preOrder()

def _check(min, root, max):
    if root == None:
        return True
    if not min < root.data < max:
        return False
    return _check(min, root.left, root.data) and _check(root.data, root.right, max)

def checkBstValidity(root):
    infinity = 10**10
    return _check(-infinity, root, infinity)
