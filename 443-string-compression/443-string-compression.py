class Solution:
    def compress(self, a: List[str]) -> int:
        newLen = 0
        
        n = len(a)
        i=0
        writeIndex = 0
        
        while i<n:
            tempCount = 0
            char = a[i]
            while i<n-1 and a[i]==a[i+1]:
                i+=1
                tempCount+=1
            
            tempCount+=1
            i+=1
            # basically we have now covered from a[i]...a[i+1]
            
            if tempCount == 1:
                newLen+=1
                a[writeIndex]=char
                writeIndex+=1
            else:
                newLen += 1
                a[writeIndex] = char
                writeIndex+=1
                # for ther char
                newLen += len(str(tempCount))
                
                for ele in str(tempCount):
                    a[writeIndex] = ele
                    writeIndex+=1
        
        return newLen