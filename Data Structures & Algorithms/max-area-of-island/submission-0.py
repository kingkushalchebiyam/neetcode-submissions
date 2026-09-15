class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0

        directions = [(1, 0), (-1, 0), (0,1), (0,-1)]

        rowLength = len(grid)
        colLength = len(grid[0])

        

        for r in range(rowLength): 
            for c in range(colLength): 
                
                if grid[r][c] == 1: 
                    stack = [(r, c)]
                    localArea = 0
                    grid[r][c] = 0


                    while stack: 
                        row, col = stack.pop()
                        localArea += 1

                        for dr, dc in directions: 
                            nr = dr + row
                            nc = dc + col

                            if (0 <= nr < rowLength and 0<= nc < colLength and grid[nr][nc] == 1):
                                grid[nr][nc] = 0
                                stack.append((nr, nc))
                        
                    maxArea = max(localArea, maxArea)
        
        return maxArea
            


        