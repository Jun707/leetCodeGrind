class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        queue = deque()
        visited = set()
        queue.append((0,0,1))
        visited.add((0,0))
        directions = [[0,1],[0,-1],[1,0],[-1,0], [1,1], [-1,1], [-1,-1],[1,-1]]
        while queue:
            r,c,length = queue.popleft()

            if r >= n or c >= n or c <0 or r < 0 or grid[r][c] == 1:
                continue
            
            if r == n-1 and c == n-1:
                return length
            
            for dr, dc in directions:
                if (r + dr,c + dc) not in visited:
                    queue.append((r+dr, c+dc, length +1))
                    visited.add((r+dr, c+dc))
        return -1