class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hashMap = {} # ele -> last 
        
        res = 0
        start = 0
        n = len(s)
        
        for i in range(n):
            
            if len(hashMap.keys())<2:
                if s[i] in hashMap:
                    hashMap[s[i]]+=1
                else:
                    hashMap[s[i]]=1
                
            else:
                if s[i] in hashMap:
                    hashMap[s[i]]+=1
                else:
                    # so we try to shrink it until we hjave a counter that becomes
                    res = max(res,i-start)
                    while start<i:
                        temp = hashMap[s[start]]
                        
                        if temp <= 1:
                            del hashMap[s[start]]
                            start = start+1
                            break
                        else:
                            hashMap[s[start]]-=1
                        start = start+1
                    #print(start)
                    hashMap[s[i]] = 1
            #print(i,hashMap,res,start)
        i+=1            

        res = max(res,i-start)
            
        return res
                            
            
          
                    
                    
                    
            