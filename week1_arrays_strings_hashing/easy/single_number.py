class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
 # XOR Operator: If finds same number it turns it to 0 and only tell the unique number
        for num in nums:
            result^=num 
        
        return result