from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        
        for index,val in enumerate(strs):
            arrangedStr = ''.join(sorted(val))
            
            cache[arrangedStr].append(index)
        res = []
        for key in cache:
            temp = []
            for val in cache[key]:
                temp.append(strs[val])
            res.append(temp)
        
        return res
        
        