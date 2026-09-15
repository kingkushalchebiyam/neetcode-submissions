class Solution:
    def floodFill(self, image: List[List[int]], sr
        : int, sc: int, color: int) -> List[List[int]]:


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rowLength = len(image)
        colLength = len(image[0])


        originalColor = image[sr][sc]

        if originalColor == color: 
            return image
        
        stack = [(sr, sc)]

        while stack: 
            r, c = stack.pop()

            image[r][c] = color

            for dr, dc in directions: 
                nr = r + dr
                nc = c + dc

                if(0 <= nr < rowLength and 0 <= nc  < colLength and image[nr][nc] == originalColor): 
                    stack.append((nr, nc))
                
        
        return image
        

       

             


        