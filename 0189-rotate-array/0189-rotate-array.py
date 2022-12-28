class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # brute force 0(n) * k
        # for i in range(0, k):
        #     nums.insert(0, nums[-1])
        #     nums.pop()
            
        rotated_array = [0] * len(nums)

        for i in range(len(nums)):
            rotated_array[(i + k) % len(nums)] = nums[i]    # adds items to array, and overflow gets 
                                                            # added to front

        nums[:] = rotated_array