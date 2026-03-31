class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sorting as per the -ve and +ve values
        nums.sort()
        result = []

        for i in range(len(nums)):
            #skip duplicate values for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # For non duplicate values
            left = i+1
            right = len(nums) - 1

            #now solve like two sum
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total  == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # move both pointer and skip duplicates
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left+=1

                    while left<right and nums[right] == nums[right+1]:
                        right-=1

                elif total < 0:
                    #need bigger sum then move left forward
                    left += 1
                else:
                    #need bigger sum then move left forward
                    right -= 1
        return result

# Time Complexity : n logn (logn) = n^2
