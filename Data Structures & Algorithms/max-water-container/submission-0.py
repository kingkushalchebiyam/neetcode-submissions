class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) -1
        maxArea = 0

        while L < R:
            localWidth = min(heights[L], heights[R])
            localArea = (R - L) * localWidth

            if localArea > maxArea: 
                maxArea = localArea
            
            if heights[R] <= heights[L]: 
                R -= 1
            else: 
                L += 1
        
        return maxArea








        
        