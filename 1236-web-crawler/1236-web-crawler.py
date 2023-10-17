# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        queue = [startUrl]
        
        def findHostName(url):
            res = list(url.split('/'))
            host = res[2]
            return host
       
        startHostName = findHostName(startUrl)
        seen = set()
        
        while queue:
            url = queue.pop(0)
            
            if url in seen:
                continue
            
            seen.add(url)
            
            urlList = htmlParser.getUrls(url)
            
            for nextUrl in urlList:
                if findHostName(nextUrl) == startHostName and nextUrl not in seen:
                    queue.append(nextUrl)
                    
                    
        return list(seen)
        