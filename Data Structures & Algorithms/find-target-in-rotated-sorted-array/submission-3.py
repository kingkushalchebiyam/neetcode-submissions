class Solution:
    def search(self, nums: List[int], target: int) -> int:
       # [3, 4, 5, 6, 1, 2]
          #l  m      r  

        #target = 4



        L = 0
        R = len(nums) - 1
        minimumIndex = 0

        while L < R: 
            M = L + (R - L) // 2

            if nums[M] < nums[R]: 
                R = M
            else: 
                L = M + 1

        pivot = L

        l = 0
        r = len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]: 
            l = pivot
        else: 
            r = pivot - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return -1

        
        
       