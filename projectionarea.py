class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans=0
        for i in range(len(grid)):
            bestr=0
            bestc=0
            for j in range(len(grid)):
                if grid[i][j]:
                    ans+=1
                bestr=max(bestr,grid[i][j])
                bestc=max(bestc,grid[j][i])
            ans+=bestc+bestr
        return ans
        
