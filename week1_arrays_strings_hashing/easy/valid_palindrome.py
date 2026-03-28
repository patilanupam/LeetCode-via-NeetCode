def isPalindrome(s):
    left = 0
    right = len(s) - 1
    # thinking: compare characters from both ends moving inward

    while left < right:
        # skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1

        # skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # compare characters ignoring case
        if s[left].lower() != s[right].lower():
            return False  # mismatch → not palindrome

        # move both pointers inward
        left += 1
        right -= 1

    return True

# Time Complexity: O(n) - we go through the string once
# Space Complexity: O(1) - we only use a few pointers, no extra space