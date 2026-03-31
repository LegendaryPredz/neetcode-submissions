class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # First we create a seen set. Sets can't contain duplicates. 
        seen = set()

        # We loop through each number in the list
        for num in nums:
            # check if its in the seen set 
            if num in seen:
                # if a number is already in the seen set then we return true 
                # as we know their is a duplicate
                return True
            # if not we add it to the set
            seen.add(num)
        
        # no duplicate found so we return false
        return False