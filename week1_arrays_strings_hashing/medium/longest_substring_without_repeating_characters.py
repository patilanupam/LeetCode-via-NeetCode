class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()

        left = 0
        max_length = 0

        # AS we are ddoing traversal to right
        #Each time we pop left and insert right whenever chars are repeating

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            
            char_set.add(s[right])

            max_length = max(max_length, right -left +1)

        return max_length
