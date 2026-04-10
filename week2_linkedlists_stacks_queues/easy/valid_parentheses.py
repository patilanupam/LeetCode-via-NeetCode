class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        #mapping closing and opening 

        mapping = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            #if opening bracket ->push
            if char in mapping.values():
                stack.append(char)
            else:
             if not stack or stack[-1] != mapping[char]:
                    return False
             stack.pop()
        
        return len(stack) == 0
