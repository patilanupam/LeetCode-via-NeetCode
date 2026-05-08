class TimeMap(object):

    def __init__(self):
        #Store the key
        self.store = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        # If key is not then register the key with new array
        if key not in self.store:
            self.store[key] = []
        #Either add the timestamp and value into that key
        self.store[key].append((timestamp,value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""
        
        values = self.store[key]

        #Exactly like Binary search but with key value pair like a dictionary
        left, right = 0, len(values)-1
        result= ""

        while left<=right:

            mid = (left+right) //2

            if values[mid][0] <=timestamp:
                result = values[mid][1]
                
                left = mid + 1
            else:
                right = mid - 1
        
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
