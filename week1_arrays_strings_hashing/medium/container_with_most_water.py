class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        # We need maxinimum volume of water so considering end values in array
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            # Storing max_area from all the possibilities
            max_area = max(max_area, area)

            # We need to do traversal from left to right in order to find max area
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
            
        return max_area
