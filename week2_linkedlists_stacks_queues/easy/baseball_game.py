# Baseball Game
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        num = 0
        total = 0
        for op in operations:
            if op == 'C':
                if stack:
                    stack.pop()
            elif op == 'D':
                num = stack[-1] * 2
                stack.append(num)
            elif op == '+':
                num = stack[-1]+stack[-2]
                stack.append(num)
            else:
                stack.append(int(op))
        
        return sum(stack)
