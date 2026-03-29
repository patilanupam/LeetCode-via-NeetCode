class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0 #This is a pointer in array

        #First case to check non-zero position and shift them in the starting of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        #Second case after moving non-zero numbers to the front replace it with the last position of non-zero number
        for i in range(insert_pos, len(nums)):
                nums[i] = 0

# Time Complexity-> O(2n) = O(n)