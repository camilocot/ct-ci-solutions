# Given a Binary Tree, write a function that returns the size of the largest
# subtree which is also a Binary Search Tree (BST). If the complete Binary Tree is BST,
# then return the size of the whole tree.
#  https://www.geeksforgeeks.org/largest-bst-binary-tree-set-2/


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Helper():
    def __init__(self):
        self.lower = float('-inf')
        self.upper = float('inf')
        self.isBst = False
        self.size = 0


def helper(node):
    c = Helper()
    if node == None:
        c.isBst = True
        return c

    l = helper(node.left)
    r = helper(node.right)

    # current subtree's boundaries
    c.lower = max(node.val, l.lower)
    c.upper = min(node.val, r.upper)

    # check left and right subtrees are BST or not
    # check left's upper again current's value and right's lower against current's value
    if l.isBst and r.isBst and node.val > l.lower and node.val < r.upper:
        c.isBst = True
        c.size = 1 + l.size + r.size

    else:
        c.size = max(l.size, r.size)

    print(c.size, node.val)

    return c


def largest_bst(node):
    return helper(node).size


""" Let us construct the following Tree
       50
     /    \
  15       60
 /  \     /  \
5   20   45    70
              /  \
            65    80
"""
root = Node(50)
root.left = Node(30)
root.right = Node(60)
root.left.left = Node(5)
root.left.right = Node(20)
root.right.left = Node(45)
root.right.right = Node(70)
root.right.right.left = Node(65)
root.right.right.right = Node(80)


print("Size of the largest BST is",
      largest_bst(root))
