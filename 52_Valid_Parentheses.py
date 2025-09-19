class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping.values():
                stack.append(char)  # apertura
            elif char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                return False  # carácter inválido
        
        return not stack
