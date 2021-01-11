class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(row: int, col:int, index: int):
            if row < 0 or row == m or col < 0 or col == n:
                return
            if grid[row][col] != -1:
                return
            grid[row][col] = index + 1
            islands[index].add((row,col))
            helper(row - 1, col, index)
            helper(row + 1, col, index)
            helper(row, col - 1, index)
            helper(row, col + 1, index)
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        islands = []
        i = 0
        for r in range(m):
            for c in range(n):
                grid[r][c] = -1 if grid[r][c] == 1 else 0
        for r in range(m):
            for c in range(n):
                islands.append(set())
                helper(r, c, i)
                i += 1
        max_size = 0;
        for island in islands:
            size = len(island)
            max_size = max(max_size, size)
        return max_size
