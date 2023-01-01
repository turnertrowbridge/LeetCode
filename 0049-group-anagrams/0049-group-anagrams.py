class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rev_hash = dict()
        anagrams_list = []

        for s in strs:
            s_sort = "".join(sorted(s))
            if s_sort not in rev_hash:
                rev_hash[s_sort] = []
            
            rev_hash[s_sort].append(s)

        for i in rev_hash:
            anagrams_list.append(rev_hash[i])

        return anagrams_list

        
    
