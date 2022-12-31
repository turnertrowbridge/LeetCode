class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # count all the characters in s1
        counter, window = Counter(s1), len(s1)              
        

        for i in range(len(s2)):
            # if the character is found in counter decrease it's count by 1
            if s2[i] in counter:                            
                counter[s2[i]] -= 1

            # if the we have gone past the window, re-add a previously checked off char
            if i >= window and s2[i - window] in counter:   
                counter[s2[i - window]] += 1

            # check if all the chars have been checked off
            if all([counter[i] == 0 for i in counter]): 
                return True
        
        return False
