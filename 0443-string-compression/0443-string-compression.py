class Solution:
    def compress(self, chars: List[str]) -> int:
        # Challenge is we have to do it in place with no extra memeory
        
        prevChar = chars[0]
        count = 1
        start = 0
        chars.append('EOL')
        n = len(chars)
        
        for i in range(1,n):
            currChar = chars[i]
            
            if prevChar == currChar:
                count+=1
                
            else:
                chars[start] = prevChar
                if count >1:
                    start = start+1
                    for ele in str(count):
                        chars[start] = ele
                        start+=1
                else:
                    start+=1
                count = 1
                prevChar = currChar
                
                
        
        return start
    