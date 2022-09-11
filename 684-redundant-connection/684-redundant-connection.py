class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # We can make use of union find the edge that casuses the formation of graph can be flagged out
        
        n = len(edges)
        
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)
        
        def findRoot(x):
            if parent[x]==x:
                return x
            val = findRoot(parent[x])
            parent[x] = val
            return val
        
        def union(x,y):
            rootX = findRoot(x)
            rootY = findRoot(y)
            
            if rootX==rootY:
                return True
            else:
                if rank[rootY] > rank[rootX]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    if rank[rootX]==rank[rootY]:
                        rank[rootX]+=1
                return False
            
        for x,y in edges:
            if not union(x,y):
                continue
            else:
                return [x,y]
            