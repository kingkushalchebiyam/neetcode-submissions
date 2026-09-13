class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

      

        for num in nums: 
            if num - 1 not in seen: 
                next_num = num + 1
                length = 1

                while next_num in seen: 
                    length += 1
                    next_num += 1
                
                longest = max(longest, length)
        
        return longest





       



            

       




                 







          

        
        