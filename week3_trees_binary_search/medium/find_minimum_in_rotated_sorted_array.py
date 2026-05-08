class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1

        #Narrowing to search to left part
        while left < right:
            #Calclate the mid value it will be same as normal Binary Search
            
            mid = (left + right)  // 2
            
            #This is same as when there is rotated sorted array
            if nums[mid] > nums[right]:
                left = mid + 1
            # This changes as now we are setting mid = right as the condition is till left < right
            else:
                right = mid
        #Always left will be the minimum value in any rotated sorted array after the iteration
        return nums[left]
