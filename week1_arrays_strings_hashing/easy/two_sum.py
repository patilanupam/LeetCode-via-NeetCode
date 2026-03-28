def twoSum(nums, target):
    seen = {}  # stores number -> index

    for i in range(len(nums)):
        complement = target - nums[i]  # what we need to reach target

        # if we've already seen the needed number, we found the pair
        if complement in seen:
            return [seen[complement], i]

        # store current number with its index for future lookup
        seen[nums[i]] = i

# Thinking:
# Instead of checking all pairs, we remember past numbers and directly check if the required complement exist

# Time Complexity: O(n)
# Space Complexity: O(n)