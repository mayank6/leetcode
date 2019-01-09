"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans=[]
        i=0
        q=[root,]
        k=len(q)
        while(q):
            l=[]
            while i<k:
                x=q.pop(0)
                l.append(x.val)
                i+=1
                if x.children:
                    q.extend(x.children[::1])
            k=len(q)
            i=0
            ans.append(l)
        return ans
