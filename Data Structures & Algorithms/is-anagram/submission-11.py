class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check to see if both strings are same size; 
        # if not then we know they aren't anagrams 
        if len(s) != len(t):
            return False

        #two empty hashmaps
        countS, countT = {}, {}

        #key, value = char, count 
        for i in range(len(s)):
            # add 1 to the value (count) of each key (char) in map
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #compare each hashmap
        return countS == countT 
        

        # Time complexity: O(n + m); where n is length of s and m is length of string t 
        # Space complexity: O(1); since we have at most 26 different characters