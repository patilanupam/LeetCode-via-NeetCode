def containsDuplicate(nums):
    seen = set()
    # thinking: set only stores unique elements

    for num in nums:
        if num in seen:
            # if already seen → duplicate exists
            return True

        seen.add(num)  # store for future comparison

    return False

# Time Complexity: O(n) - we go through the list once
# Space Complexity: O(n) - at most n unique elements