class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

# Thinking: The main idea is to sort the word into distinct characters and compare it with a key-value pair in group and add the same words which is made of same chars in same list
        groups = {}

        for word in strs:

            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)
        
        return groups.values()

   
        
