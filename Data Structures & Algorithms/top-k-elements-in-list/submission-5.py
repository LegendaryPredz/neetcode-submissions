class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # array of len(nums) + 1 arrays
        freq = [[] for i in range(len(nums) + 1)]
        
        # patttern for counting number of key (num) the dict
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        # .items returns [key, value]. Use this to append each num that 
        # appears cnt amount of times to the bucket that represents the cnt amount
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        # loop backwards through the freq array 
        # its in sorted order 
        for i in range(len(freq) - 1, 0, -1):
            # for each num that appears in the kth most frequent bucket
            # append that to the list and return it
            for num in freq[i]:
                res.append(num)
                if len(res) == k: 
                    return res
        

        # Time complexity: O(n)
        # Space complexity: O(n)