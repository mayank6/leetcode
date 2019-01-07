class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        a=[]
        if (len(nums) == 0 or r * c != len(nums) * len(nums[0])):
            return nums
        x = [[None for i in range(c)] for j in range(r)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                a.append(nums[i][j])
        
        for i in range(r):
            for j in range(c):
                x[i][j]=a.pop(0)
        return x
