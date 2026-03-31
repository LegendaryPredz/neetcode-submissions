class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # target - num = key in hashmap 
       # return index of key and current index

        
        prevMap = {}
        # loop through nums getting index and currnet num (n)
        for i, n in enumerate(nums):
            # find the diff using target - current num (n)
            diff = target - n
            #if the diff is already in the map, then return the index of the diff key
            #and the current index 
            if diff in prevMap:
                return [prevMap[diff], i]
            # else we need to add the new key (current num) and its value (current index)
            prevMap[n] = i
            