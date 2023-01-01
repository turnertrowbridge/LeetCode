class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s = Counter()
        count_t = Counter()
        
        for i in range(len(s)):
            count_s[s[i]] += 1
            count_t[t[i]] += 1
        
        print(count_s)
        print(count_t)

        return count_s == count_t