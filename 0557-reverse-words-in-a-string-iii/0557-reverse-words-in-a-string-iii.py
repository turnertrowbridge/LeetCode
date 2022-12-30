# copied from a codebrah's solution to get understanding


class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_s = ""
        current_word = []
        
        for c in s:
            if c == " ":
                reversed_s += self.reverseWord(current_word) + " "
                current_word = []
            else:
                current_word.append(c)
                
        return reversed_s + self.reverseWord(current_word)
    
    def reverseWord(self, word: List[int]) -> str:
        l, r = 0, len(word) - 1
        
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        
        return "".join(word)