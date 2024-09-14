from collections import deque


class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def leftView(root):

    if root is None:
        return
    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        i = 0
        while i < size:
            curr = queue.popleft()
            i = i + 1

            if i == 1:
                print(curr.key, end=' ')

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    leftView(root)
