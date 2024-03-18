class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def mergeInterval(interval1, interval2):
            max1,min1 = interval1
            max2,min2 = interval2

            return (max(max1,max2), min(min1,min2))
        

        stack = []

        for ele in arr:

            currPart = (ele,ele)

            while stack and not (currPart[0] >= stack[-1][0] and currPart[1] >= stack[-1][0]):
                prevPart = stack.pop()
                currPart = mergeInterval(prevPart,currPart)

            stack.append(currPart)

        return len(stack) 