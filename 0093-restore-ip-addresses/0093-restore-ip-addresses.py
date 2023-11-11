class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # So at each point we can either pickup 1,2,3 no from the s
        
        res = []
        n = len(s)
        
        def obtainIp(sIndex,currRes):
            
            if sIndex == n:
                if len(currRes) == 4:
                    res.append(currRes)
                return 
            
            # Edge case if the current element is a 0 we can only take it as 1
            
            # Taking only 1
            obtainIp(sIndex+1,currRes+[s[sIndex]])
            
            if s[sIndex] !='0':
                # then we can try for 2 or 3 characters
                
                if sIndex+1 < n:
                    obtainIp(sIndex+2, currRes+[s[sIndex:sIndex+2]])
                
                if sIndex+2< n and int(s[sIndex:sIndex+3]) <=255:
                    obtainIp(sIndex+3, currRes+[s[sIndex:sIndex+3]])
        
        obtainIp(0,[])
        return ['.'.join(ele) for ele in res]

                    