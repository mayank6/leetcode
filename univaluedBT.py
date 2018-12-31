# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        value,stack=root.val,[root,]
        while stack:
            root=stack.pop(0)
            if root is not None:    
                if root.val !=value:
                    return False
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)
        return True
