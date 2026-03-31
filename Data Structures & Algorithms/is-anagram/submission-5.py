class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # First we check to see if each string is the same length; 
    # If not then we know it can't be a valid anagram
       if len(s) != len(t):
        return False

    # We create two dictionaries for both string S and string T to keep track
    # of each letter and its number of occurences
       countS, countT = {}, {}

    # Loop through the size of len(s) as we know by this point that each string
    # is the same size
       for i in range(len(s)):
        # Going through each string and adding their characters and occurences 
        # to their respective dictionaries
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    # Comparing both dictionaries to see if they are the same. If not, then we
    # then we know its not a valid anagram
       return countS == countT