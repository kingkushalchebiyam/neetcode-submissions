class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}

        stack = []

        if len(s) == 1 or len(s) == 0: 
            return False

        for char in s: 
            if char in mapping: 
                if stack and stack[-1] == mapping[char]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(char)
        
        if stack: 
            return False
        
        return True

        

        