# Determine whether a tree is a valid binary search tree.
# https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
# https://www.youtube.com/watch?v=MILxfAbIhrE

#  Traverses down the tree keeping track of the narrowing min and max allowed values as it goes,
#  looking at each node only once.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


INT_MAX = 4294967296
INT_MIN = -4294967296


def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))


def isBSTUtil(node, mini, maxi):

    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data+1, maxi))


def is_bst(root):
    maximux = float('inf')
    minimun = float('-inf')

    # Retusn true if the given tree is a BST and its values
    # >= min and <= max
    def helper(root, minimun, maximux):

        if root is None:
            return True
        # Check the subtrees recursively
        if root.data > minimun and root.data < maximux:
            return helper(root.left, minimun, root.data) and helper(root.right, root.data, maximux)
        # False if this node violates min/max constraint
        return False

    return helper(root, minimun, maximux)


# Driver program to test above function
root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(4)

print(is_bst(root))
