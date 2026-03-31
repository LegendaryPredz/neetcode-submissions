class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #each string will be encoded with the lenght of the string as
            #well as the delimeter '#'
            #e.g. 4#neet4#code4#love3#you
            res += str(len(s)) + "#" + s 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i # we need a second pointer
            while s[j] != "#": # while j doesnt equal the # we encoded the string with then we keep going
                j += 1
            length = int(s[i:j]) # j is on the # so we can; j is exclusive
            #return the length of the string which is the number we put at the front
            i = j + 1 # set i = the beginning of the word
            j = i + length # set j = the end of the length of the next word
            res.append(s[i:j]) # append the word; j is on the length of the next word but its exclusive
            i = j # set i = j, which is the length value of the next word
        return res
