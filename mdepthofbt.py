# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack=[(1,root)]
        highest=0
        while stack:
            depth,root=stack.pop()
            
            if root is not None:
                highest=max(highest,depth)
                stack.append((depth+1,root.left))
                stack.append((depth+1,root.right))
        return highest
