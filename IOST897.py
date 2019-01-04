# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ans=[]
        def inorder(root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
            return ans
        inorder(root)
        curr=cur=TreeNode(None)
        for i in ans:  
            cur.right=TreeNode(i)
            cur=cur.right
        return curr.right
