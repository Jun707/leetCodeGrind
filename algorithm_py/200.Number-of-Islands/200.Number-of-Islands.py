class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i ,j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < len(grid) and j < len(grid[0]) and i >= 0 and j >= 0 and grid[i][j] == "1":
            grid[i][j] = 0
            self.dfs(grid, i-1, j)
            self.dfs(grid, i+1, j)
            self.dfs(grid, i, j-1)
            self.dfs(grid, i , j+1)