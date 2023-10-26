class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashMap = {}
        
        for index,value in enumerate(s):
            hashMap[value] = index
            
        # So now we have the last occuring indexes of each of the character
        n = len(s)
        maxIndex = 0
        start = 0
        res = []
        
        for i in range(n):
            maxIndex = max(maxIndex,hashMap[s[i]])
            
            if maxIndex==i:
                # We can close out the older partition and start a new one
                res.append(i-start+1)
                start = i+1
                maxIndex = 0
                
        return res 
                
            
            
                
                
            
            
        