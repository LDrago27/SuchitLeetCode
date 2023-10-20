class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strList = []
        for index,string in enumerate(strs):
            if string > string[::-1]:
                strList.append(string)

            else:
                strList.append(string[::-1])
                

        n = len(strList)        
        ans = ''
        for i in range(n): 
            rev = strList[i][::-1]
            rest = "".join(strList[i+1:] + strList[:i])
            for k in range(len(strList[i])): 
                ans = max(ans, strList[i][k:] + rest + strList[i][:k])
                ans = max(ans, rev[k:] + rest + rev[:k])
        return ans 
        
