import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # Binary Search example based on values not Index

        #Initiating left and right same as Binary search based on requirement
        left = 1
        #Max value as we maximum speed or k is max(piles) value
        right = max(piles)

        result = right

        while left <= right:
            #Median value set meaning in array of [3,6,7,11] the mid will be 6 as (1 + 11) // 2 = 6 so k =6
            k = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(float (pile) / k)

            if hours <= h:
                    # Case of fast speed
                result = k
                    #AS we need minimum best value less than the mid value of k for optimal solution
                right = k - 1

                # Too slow increase the spped
            else:
                left = k + 1
        
        return result
