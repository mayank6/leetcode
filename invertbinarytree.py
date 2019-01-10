# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        temp=None
        stack=[root,]
        while stack:
            node=stack.pop(0)
            if node:
                temp=node.left
                node.left=node.right
                node.right=temp
                stack.append(node.left)
                stack.append(node.right)
        return root
