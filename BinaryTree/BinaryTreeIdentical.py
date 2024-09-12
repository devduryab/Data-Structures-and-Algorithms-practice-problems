# A class to store a binary tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def isIdentical(x, y):

    if x is None and y is None:
        return True

    return (x is not None and y is not None) and (x.key == y.key) and \
        isIdentical(x.left, y.left) and isIdentical(x.right, y.right)


x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

# construct the second tree
y = Node(15)
y.left = Node(10)
y.right = Node(20)
y.left.left = Node(8)
y.left.right = Node(12)
y.right.left = Node(16)
y.right.right = Node(25)

if isIdentical(x, y):
    print('The given binary trees are identical')
else:
    print('The given binary trees are not identical')
