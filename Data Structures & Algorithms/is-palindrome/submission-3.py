class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum(): 
                newS += char.lower()


        pointer1 = 0
        pointer2 = len(newS) - 1

        while pointer1 < pointer2: 
            if newS[pointer1] == newS[pointer2]:
                pointer1 += 1
                pointer2 -= 1 
                continue
            else: 
                return False
        
        return True



        


        
        