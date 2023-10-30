class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1List = list(version1.split('.'))
        v2List = list(version2.split('.'))
        
        n = len(v1List)
        m = len(v2List)
        
        def padList(arr,length):
            if len(arr) == length:
                return arr
            else:
                l1 = len(arr)
                for _ in range(length-l1):
                    arr = arr + ['0']
                return arr
        maxLen = max(n,m)
        v1List,v2List = padList(v1List,maxLen),padList(v2List,maxLen)
        
        for i in range(maxLen):
            
            if int(v1List[i]) > int(v2List[i]):
                return 1
            elif int(v1List[i]) < int(v2List[i]):
                return -1
            
        return 0