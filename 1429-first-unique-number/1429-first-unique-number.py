from collections import Counter
class FirstUnique:

    def __init__(self, nums: List[int]):
        
        ctr = Counter(nums)
        self.queue = []
        self.counter = {}
        
        for ele in nums:
            if ctr[ele] == 1:
                self.queue.append(ele)
            self.counter[ele] = ctr[ele]
        
        

    def showFirstUnique(self) -> int:

        while self.queue and self.counter[self.queue[0]] != 1 :
            self.queue.pop(0)
        
        if self.queue:
            return self.queue[0]
        return -1
        

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.counter[value] = self.counter.get(value,0)+1

        
        
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)