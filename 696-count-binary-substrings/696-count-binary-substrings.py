class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # make groups of contiguos element
        # wheneever a change in groups occurs we can only make min groups, value
        
        
        groups = [1]
        n = len(s)
        
        for i in range(1,n):
            
            if s[i]==s[i-1]:
                groups[-1]+=1
            else:
                groups.append(1)
        
        n1 = len(groups)
        res = 0
        for i in range(1,n1):
            res+= min(groups[i],groups[i-1])
        return res