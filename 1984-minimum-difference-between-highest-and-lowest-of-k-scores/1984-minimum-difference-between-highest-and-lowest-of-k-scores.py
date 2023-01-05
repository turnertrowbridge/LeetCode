class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        i, j = 0, k - 1
        nums.sort()

        min_dif = nums[len(nums)-1] - nums[0] # max possible dif
    
        while j < len(nums):
            min_dif = min(min_dif, nums[j] - nums[i])

            i += 1
            j += 1


        return min_dif
    


