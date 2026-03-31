class Solution:
    # can be empty string; return 0 
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: 
            return 0 
        if len(s) == 1:
            return 1

        letters = set()
        l = 0
        r = 0 
        currLongest = 0
        while r <= len(s) - 1:
            if s[r] not in letters:
                letters.add(s[r])
                r += 1
                currLongest = max(currLongest, len(letters))
            else:
                letters.remove(s[l])
                l += 1
                
        return currLongest 
            