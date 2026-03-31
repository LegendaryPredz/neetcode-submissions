class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if prevMap[diff]:
                return [prevMap[diff], i + 1]
            prevMap[numbers[i]] = i + 1
        return []