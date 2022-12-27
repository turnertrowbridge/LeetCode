class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #for i, x in enumerate(nums):
        #    nums[i] = x * x
        #return sorted(nums)
        result = [-1] * len(nums)  # intialize an "empty" array of the same length as nums
        left = 0        
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):      # loop: start, stop, step
            if abs(nums[left]) > abs(nums[right]):  # check the absolute value of each side
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
        
        return result
