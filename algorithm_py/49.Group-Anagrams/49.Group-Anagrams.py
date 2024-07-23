class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp not in strs_dict:
                strs_dict[temp] = []
            strs_dict[temp].append(s)
        
        return list(strs_dict.values())