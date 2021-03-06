"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack,output=[root,],[]
        
        while stack:
            root=stack.pop()
            if root is not None:
                output.append(root.val)
            stack.extend(root.children[:])
        return output[::-1]
            
