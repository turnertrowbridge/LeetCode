# used GitHub Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_seen = Counter()

        left = right = 0
        max_substring = 0 

        while right < len(s):  
            r = s[right] # get character to the right
            chars_seen[r] += 1 # save right character and increase count by 1

            while chars_seen[r] > 1: # once a character is seen twice
                l = s[left] # get character at left
                chars_seen[l] -= 1 # decrease count by 1
                left += 1 # move left to next character

            # keep max substring or replace 
            # or add new max substring
            max_substring = max(max_substring, right - left + 1) 
 
            right += 1 # move right to next character
        return max_substring


            

