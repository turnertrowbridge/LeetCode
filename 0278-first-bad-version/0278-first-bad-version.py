# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# <- false
# true ->

# 0 1 2 3 !4 5

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while ((l < r)):
            mid = math.floor( l + (r - l) / 2)

            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1

        return l