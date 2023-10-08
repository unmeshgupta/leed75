class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_map = {')':'(',']':'[','}':'{'}

        for c in s:
            if c in dict_map:
                if stack and stack[-1] == dict_map[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return True if not stack else False
