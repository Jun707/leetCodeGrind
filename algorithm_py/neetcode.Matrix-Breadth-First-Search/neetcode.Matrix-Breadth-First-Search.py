class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        length = 0

        visited = set()
        queue = deque()
        visited.add((0, 0))
        queue.append((0, 0))
        rows = len(grid)
        cols = len(grid[0])

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
            
                directions = [[0,1], [0, -1], [1,0], [-1, 0]]
                for dc, dr in directions:
                    r = dr + r
                    c = dc + c
                    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 1 or (r,c) in visited:
                        continue
                    queue.append((r,c))
                    visited.add((r,c))
            length +=1
        return -1