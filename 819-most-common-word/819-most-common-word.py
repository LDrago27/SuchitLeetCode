from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        
        paragraph=paragraph.replace('!',' ')
        paragraph=paragraph.replace('?',' ')
        paragraph=paragraph.replace(',',' ')
        paragraph=paragraph.replace(';',' ')
        paragraph=paragraph.replace('.',' ')
        paragraph=paragraph.replace("'",' ')
        paragraph=paragraph.strip()
        paragraph = paragraph.split(' ')
        c = Counter(paragraph)
        key = list(c.keys())
        key.sort(key = lambda x: -c[x])
        print(key)
        for k in key:
            if k not in banned and k!='':
                return k
        
        