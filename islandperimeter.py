class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        def sum_adjacent(i, j):
                    adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
                    res = 0
                    for x, y in adjacent:
                        if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                            res += 1
                    return res

        count = 0
        for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if grid[i][j] == 1:
                            count += sum_adjacent(i, j)
        return count

    #-----------------------------------------------------------------------#
    class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans=0
        row,col=len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
               if grid[i][j]==1:
                ans+=4
                if i-1>=0 and grid[i-1][j]==1:
                    ans-=1
                if i+1<row and grid[i+1][j]==1:
                    ans-=1
                if j+1<col and grid[i][j+1]==1:
                    ans-=1
                if j-1>=0 and grid[i][j-1]==1:
                    ans-=1
        return ans
