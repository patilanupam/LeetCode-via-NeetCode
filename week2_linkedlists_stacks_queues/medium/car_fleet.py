# Car Fleet

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        #Pair postion and speed
        cars = list(zip(position, speed))

        #Sort based on position descending that's why reverse = true
        cars.sort(reverse = True)

        stack = []

        for pos, spd in cars:

            time = (target - pos) / spd

            #If current car takes longer --> new fleet

            if not stack or time > stack[-1]:
                stack.append(time)

            #else --> it join existing fleet --> do nothing
        
        return len(stack)


            


        
