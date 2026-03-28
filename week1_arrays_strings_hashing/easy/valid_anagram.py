def isAnagram(s, t):
    # if lengths differ, impossible to be anagrams
    if len(s) != len(t):
        return False

    count = {}

    # count frequency of each character in s
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    # reduce counts using t
    for ch in t:
        # if char not found or already used up → not an anagram
        if ch not in count or count[ch] == 0:
            return False

        count[ch] -= 1

    # if all matched correctly, counts will balance to zero
    return True

# Time Complexity: O(n) - we go through both strings once
# Space Complexity: O(n) - at most 26 letters (or 128 ASCII