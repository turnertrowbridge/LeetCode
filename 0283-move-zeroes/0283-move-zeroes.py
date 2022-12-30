class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # nums at i swap with themselves until a zero is found
                # then they swap with the last seen zero
                nums[zero], nums[i] = nums[i], nums[zero]   
                zero +=1    # increase pointer to find a zero                             



