class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
    

        row = len(grid)
        cols = len(grid[0])

        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(row): 
            for c in range(cols): 
                if grid[r][c] == "1": 
                    islands += 1

                    stack = [(r, c)]
                    grid[r][c] = "0"

                    while stack: 
                        curr_r, curr_c = stack.pop()

                        for dr, dc in directions: 
                            nr = curr_r + dr
                            nc = curr_c + dc

                            if (0 <= nr < row and 0 <= nc < cols and grid[nr][nc] == "1"): 
                                stack.append((nr, nc))
                                grid[nr][nc] = "0"
               
    
        return islands
    




        