class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        j=0
        for i in nums:
           if i==1:
            j+=1
           else:
            m=max(m,j)
            j=0
           m=max(m,j) 
        return m
