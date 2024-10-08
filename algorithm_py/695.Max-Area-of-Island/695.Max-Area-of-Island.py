class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, self.dfs(grid, i, j))
        return area

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>= len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = 0
        count = 1
        count +=self.dfs(grid, i-1, j)
        count +=self.dfs(grid, i+1, j)
        count +=self.dfs(grid, i, j-1)
        count +=self.dfs(grid, i, j+1)

        return count