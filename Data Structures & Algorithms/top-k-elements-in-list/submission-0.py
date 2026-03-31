class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Using bucket sort
        count = {} 
        freq = [[] for i in range (len(nums) + 1)] #Creating our buckets to len nums 

        #loop through each number in the array and count the number of occurences of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        #count.items returns each key-value pair as a tuple in a list
        #loop through each tuple and place the numbers in their corresponding count list
        #e.g. there  were one 1's, two 2's, and three 3's. Place 1 in the 1's list, 2 in the twos list and 3 in the threes list 
        #e.g. if there were 3 100's then 100 would get placed in the 3's list as well
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Create a result list and loop through the back of the list (sorted in ascending order by count)
        # to get the number with the highest count and append that to the list
        # do that k times and return the list.
        res = []
        for i in range (len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        