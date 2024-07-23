class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0, set())
    
    def dfs(self, grid, r, c, visit):
        rows = len(grid)
        cols = len(grid[0])

        if r == rows or c == cols or min(r,c) < 0 or (r,c) in visit or grid[r][c] == 1:
            return 0
        if r == rows -1 and c == cols-1:
            return 1
        
        visit.add((r,c))

        count = 0
        count += self.dfs(grid, r+1, c, visit)
        count += self.dfs(grid, r-1, c, visit)
        count += self.dfs(grid, r, c+1, visit)
        count += self.dfs(grid, r, c-1, visit)

        visit.remove((r,c))

        return count