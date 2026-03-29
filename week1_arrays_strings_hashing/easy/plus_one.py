class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # start from last index (rightmost digit)
        i = len(digits) - 1

        # process digits from right → left (carry logic)
        while i >= 0:

            # if current digit is less than 9 → just add 1 and finish
            if digits[i] < 9:
                digits[i] += 1
                return digits  # no carry needed, exit early

            # if digit is 9 → becomes 0, carry moves left
            digits[i] = 0
            i -= 1

        # if we reach here, all digits were 9
        # example: [9,9,9] → [1,0,0,0]
        return [1] + digits
    
# Time Complexity: O(n) - in worst case (all 9s) we go through all digits once
# Space Complexity: O(1) - we modify in place, only extra space is for