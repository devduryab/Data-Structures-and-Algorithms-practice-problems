class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return -1
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)

print("Height of the binary tree is: ", height(root))

# -------------------------------------------------------------------------------------------
# output: Height of the binary tree is:  2
