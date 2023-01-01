class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = dict()

        for i in range(len(nums)):
            dif = target - nums[i]

            if (dif in seen_map):
                return [seen_map[dif], i]
            
            seen_map[nums[i]] = i
         
