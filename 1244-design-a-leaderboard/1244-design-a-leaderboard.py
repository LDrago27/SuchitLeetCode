from heapq import heappop,heapify,heappush
class Leaderboard:
    
    def __init__(self):
        self.playerScore = {}
        self.maxHeap = [] # increasing order of (score,id)

    def addScore(self, playerId: int, score: int) -> None:
        
        # find the entry in maxHeap and remove it and then push the updated value
        self.playerScore[playerId] = self.playerScore.get(playerId,0) + score
        found = False
        for index,value in enumerate(self.maxHeap):
            score,pid = value
            if pid == playerId:
                self.maxHeap[index] = [self.playerScore[playerId]*-1,playerId]
                found = True
                break
                
        if not found:
            heappush(self.maxHeap,[self.playerScore[playerId]*-1,playerId])
        else:
            heapify(self.maxHeap)
        
        

    def top(self, K: int) -> int:
        temp = []
        res = 0
        for _ in range(K):
            score,pid = heappop(self.maxHeap)
            res += score*-1
            temp.append([score,pid])
        
        for ele in temp:
            heappush(self.maxHeap,ele)
        
        return res

    def reset(self, playerId: int) -> None:
        self.playerScore[playerId] = 0
        for index,value in enumerate(self.maxHeap):
            score,pid = value
            if pid == playerId:
                self.maxHeap[index] = [self.playerScore[playerId]*-1,playerId]
                found = True
                break
        heapify(self.maxHeap)
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)