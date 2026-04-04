class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Sorting numbers I think so
        max_length = 0

        for num in num_set:
            # Thinking:
            #This is the beginning as we are checking 2-1 = 1 is there if not then it's set to current
            if num - 1 not in num_set:
                current = num
                length = 1
            #Continue for other numbers if we found sequence
                while current + 1 in num_set:
                    current+=1
                    length+=1

                max_length = max(max_length, length)

        return max_length


# Time Complexity: O(n) as here we are checking the sequence in the array once
