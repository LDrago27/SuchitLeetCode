from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        newStr = [(index,''.join(sorted(list(value)))) for index,value in enumerate(strs)]

        res = defaultdict(list)
        for origIndex,value in newStr:
            res[value].append(strs[origIndex])
        return list(res.values())

        