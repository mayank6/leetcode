#mysolution little bit bad trying tree problem first time
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        depth=1
        highest=depth
        stacknumber,stackdepth=[root,],[depth,]
        while stacknumber:
            root,depth=stacknumber.pop(),stackdepth.pop()
            if depth>highest:
                highest=depth
            if root.children is not None:
                depth+=1
                for i in range(len(root.children)):
                    stacknumber.append(root.children[i])
                    stackdepth.append(depth)
        return highest
        
 #------------------------------------------------------------------------------#
 #recusrsive approach
 
 """
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        elif root.children==[]:
            return 1
        else:
            height=[self.maxDepth(i) for i in root.children]
            return max(height)+1
  
  
 #---------------------------------------------------------------------------#
 #with one stack only forgot that in a list we can push tuples :(
 class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        depth=1
        highest=depth
        stacknumber=[(root,1)]
        while stacknumber:
            root,depth=stacknumber.pop()
            highest=max(depth,highest)
            if root.children is not None:
                depth+=1
                for i in range(len(root.children)):
                    stacknumber.append((root.children[i],depth))
                    
        return highest
        
