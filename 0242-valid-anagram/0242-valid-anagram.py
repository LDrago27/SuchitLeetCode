from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ctrS, ctrT = Counter(s), Counter(t)

        return ctrS == ctrT
        