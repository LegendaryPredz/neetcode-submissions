class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        r = 0
        l = 0
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