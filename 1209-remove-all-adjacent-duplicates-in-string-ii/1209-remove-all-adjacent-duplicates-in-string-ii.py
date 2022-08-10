class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        temp = []
        dupNumber = 0
        lastChar = ''
        for char in s:
            if not temp:
                temp.append(char)
                dupNumber = 1
                lastChar = char
                continue
            #print(dupNumber,lastChar)

            if lastChar == char:
                dupNumber+=1
            else:
                dupNumber = 1
            temp.append(char)
            lastChar = char
            
            #print(temp,dupNumber,lastChar)
            while dupNumber == k:
                while dupNumber>0:
                    temp.pop()
                    dupNumber-=1
                #print(temp,dupNumber)
                if temp:
                    lastChar = temp[-1]
                    j = len(temp)-1
                    dupNumber = 0
                    while j>=0 and lastChar==temp[j]:
                        j-=1
                        #print('k')
                        dupNumber+=1
                else:
                    dupNumber = 0
                    lastChar = ''
        
        return ''.join(temp)
                
                
            
                
            