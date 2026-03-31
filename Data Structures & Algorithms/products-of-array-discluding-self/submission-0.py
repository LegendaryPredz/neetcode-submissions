class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #example Input : [1,2,4,6] Output : [48, 24, 12, 8]
        res = [1] * len(nums) # res = [1, 1, 1, 1]

        # res[0] = 1
        # prefix 1 * 1 = 1
        # res[1] = 1
        # prefix 1 * 2 = 2
        # res[2] = 2
        # prefix 2 * 4 = 8
        # res[3] = 8
        # res = [1, 1, 2, 8]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # res[3] 8 * 1 = 8
        # postfix 1 * 6 = 6
        # res[2] 2 * 6 = 12
        # postfix 6 * 4 = 24
        # res[1] 1 * 24 =  24
        # postfix 2 * 24 = 48
        # res[0] 1 * 48 = 48
        # res = [48, 24, 12, 8]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res