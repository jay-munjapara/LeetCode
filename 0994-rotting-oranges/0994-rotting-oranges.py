class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = collections.deque() #initial queue for storing coordinates of rotten oranges
        fresh = 0 # initial fresh orange count
        time = 0 # initial time , incremented when per unit process is completed

        ROWS = len(grid)
        COLS = len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append([row, col])

        directions = [[1,0], [-1,0], [0,1], [0,-1]] # no diagonals
        while q and fresh > 0:
            for i in range(len(q)):
                r,c  = q.popleft() # for getting most recent value / coordinates
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # checking inbound and fresh
                    if (
                        row in range(ROWS) and 
                        col in range(COLS) and 
                        grid[row][col] == 1):
                        grid[row][col] = 2 # marking this as rotten / visited
                        fresh -= 1 # reducing the fresh count
                        q.append([row,col])
            time += 1
        return time if fresh == 0 else -1