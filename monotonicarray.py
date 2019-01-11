class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        p=0
        n=0
        z=1
        for i in range(len(A)-1):
            x=A[i]-A[i+1]
            if x>0:
                p=1
            elif x<0:
                n=1
            else:
                z+=1
        if len(A)==z:
            return True
        elif p!=n:
            return True
        else:
            return False
        
            
            
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        p=True
        n=True
        for i in range(len(A)-1):
            x=A[i]-A[i+1]
            if x>0:
                p=False
            elif x<0:
                n=False
        return p or n
