class Solution:
    
    def sort_string(self, s: str):
        l = [c for c in s] 
        l.sort()
        return "".join(l)
    


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rev_hash = dict()
        anagrams_list = []

        for s in strs:
            s_sort = self.sort_string(s)
            if s_sort not in rev_hash:
                rev_hash[self.sort_string(s)] = [s]
            else:
                rev_hash[self.sort_string(s)].append(s)

        for i in rev_hash:
            anagrams_list.append(rev_hash[i])

        return anagrams_list

        
    
