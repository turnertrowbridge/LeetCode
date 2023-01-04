class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:

            # skip over non alpha numeric characters
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            
            # check if left and right are not equal when lowercase
            if s[start].lower() != s[end].lower():
                return False
            
            # move pointers
            start +=1
            end -=1

        return True
