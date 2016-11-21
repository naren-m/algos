import sys
sys.path.append('/Users/nmudivar/GDrive/python_code/personal/learning/algos')
import data_structures as ds

from data_structures import bst

def main():
    b = bst.BinarySearchTree(3)
    b.insert(5)
    b.insert(4)
    b.insert(1)
    b.inOrder()
    b.preOrder()
    print b.data
    print "Right", b.right.data
    print "Left", b.left.data
    print "Right.Left", b.right.left.data

    print b.find(3)
    print b.find(4)
    print b.find(5)
    print b.find(6)

    print bst.checkBstValidity(b)

if __name__ == '__main__':
    main()
