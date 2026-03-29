class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1 #Mapping of the indexes of each number from 1 to n

            if nums[index] > 0:
                nums[index] = -nums[index] #-ve mapping for genuine positions or not repeated numbers in array
        
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result