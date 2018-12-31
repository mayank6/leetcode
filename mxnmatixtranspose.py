class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n=len(A),len(A[0])
        ans=[[None]*m for _ in range(n)]
        
        for i,row in enumerate(A):
            for j,val in enumerate(row):
                ans[j][i]=val
        return ans
