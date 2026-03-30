class Solution:
    def isValid(self, s):
        stack = []
        
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # If closing bracket
            if char in mapping:
                top = stack.pop() if stack else '#'
                
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0