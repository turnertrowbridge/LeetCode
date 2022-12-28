class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # ** brute force **
        # time complexitiy: O(n) * k 
        # space complexity: O(1)

        # for i in range(0, k):
        #     nums.insert(0, nums[-1])
        #     nums.pop()


        # ** using another array**
        # time complexitiy: O(n) 
        # space complexity: O(n)


        # rotated_array = [0] * len(nums)

        # for i in range(len(nums)):
        #     rotated_array[(i + k) % len(nums)] = nums[i]    # adds items to array, and overflow gets 
        #                                                     # added to front

        # nums[:] = rotated_array


        # leet code solution: cyclic replacements
        # time complexitiy: O(n)
        # space complexity: O(1)

        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx] # swap elements
                current = next_idx 
                count += 1

                if start == current:
                    break
            start += 1 