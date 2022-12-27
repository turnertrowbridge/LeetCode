class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        
        while (l < r):
            mid = math.floor(l + (r - l) / 2)   # get mid value

            if (nums[mid] == target):   # if mid is target return mid
                return mid
            elif (nums[mid] < target):  # target is to the right
                l = mid + 1             # move the left to mid + 1 (since mid has already been checked)
            else:
                r = mid                 # else set r to mid
        
        return l