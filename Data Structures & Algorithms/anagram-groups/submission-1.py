class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Creating a hashmap where key is tuple of letters and values are the words that contain those letters
        for s in strs:
            count = [0] * 26 # Creating an array of 26 zeroes to be placeholders for each letterf found
            for c in s:
                count[ord(c) - ord('a')] += 1 # converting each character to their ascii values and subtracting from a(0). this will give us the place in the array 
            res[tuple(count)].append(s) # converting the array to a tuple (key) and appending the word to the value
        return list(res.values())