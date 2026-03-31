class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # empty hashmap of arrays
        res = defaultdict(list)
        #loop through each string 
        for s in strs:
            # create an array that represents the amount of each character a string has
            # 26 letters in alphabet so an array of 26 0's to begin 
            count = [0] * 26
            # loop through each string 
            for c in s: 
                # increment the position in the array that matches the position in the 
                # alphabet for each character seen
                count[ord(c) - ord("a")] += 1
            # when finished counting the characters in the string; add the key (if not already added), a tuple of
            # the characters in the str e.g. "hat" = ["a", "h", "t"]  
            # or simply append the new string to the values of the already created key
            res[tuple(count)].append(s)
            # return a list of the values of the hashmap
        return list(res.values())


        # Time complexity: O(m + n) 
        # Space complexity: O(m * n)
        # where m is number of string and n is length of longest string