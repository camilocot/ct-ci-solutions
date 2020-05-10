# Given a binary tree of integers, find the maximum path sum between two nodes.
# The path must go through at least one node, and does not need to go through the root.

# For each node there can be four ways that the max path goes through the node:
# 1. Node only
# 2. Max path through Left Child + Node
# 3. Max path through Right Child + Node
# 4. Max path through Left Child + Node + Max path through Right Child


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf")  # placeholder to be updated

        def get_max_gain(node):
            nonlocal max_path  # This tells that max_path is not a local variable
            if node is None:
                return 0

            # The important thing is "We can only get any sort of gain IF our branches are not below zero.
            # If they are below zero, why do we even bother considering them?
            # Just pick 0 in that case. Therefore, we do max(<some gain we might get or not>, 0).
            gain_on_left = max(get_max_gain(node.left), 0)
            gain_on_right = max(get_max_gain(node.right), 0)

            # the node under consideration is the root of the max path
            current_max_path = node.val + gain_on_left + gain_on_right
            max_path = max(max_path, current_max_path)

            return node.val + max(gain_on_left, gain_on_right)
        get_max_gain(root)  # Starts the recursion chain
        return max_path
