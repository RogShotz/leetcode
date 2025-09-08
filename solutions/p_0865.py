'''
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

Constraints:

The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.

'''

# Thank you https://leetcode.com/u/LeadingTheAbyss/ for the guide helping me with the solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        
        def max_depth(node):
            if not node:
                return 0
            return 1 + max(max_depth(node.left), max_depth(node.right))
        

        max_d = max_depth(root)
        # Least Common Ancestor
        def lca_dfs(node, count):
            if not node:
                return None
            if max_d - 1 == count:
                return node
            # p is parent, c is count
            left_node = lca_dfs(node.left, count+1)
            right_node = lca_dfs(node.right, count+1)

            if left_node and right_node:
                return node
            
            return left_node if left_node else right_node
        
        return lca_dfs(root, 0)
    