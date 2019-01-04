class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """  
        m,n=len(matrix[0])-1,len(matrix)-1
        for j in range(1,m+1):
            for i in range(1,n+1):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True
