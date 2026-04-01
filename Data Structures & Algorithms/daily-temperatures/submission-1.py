class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair = [temp, indx]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #stack[-1] is the top of the stack and [0] is the first value in that pair
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
