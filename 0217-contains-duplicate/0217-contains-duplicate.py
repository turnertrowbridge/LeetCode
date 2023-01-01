class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = dict()

        for i in nums:
            if i in seen:
                return True
            seen[i] = True
        
        return False