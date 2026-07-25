class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        airports=defaultdict(list)
        for s,d,p in flights:
            airports[s].append([d,p])

        self.mincost=float('inf')
        visited=set()

        def dfs(node,cost,K):
            #print(node,cost)
            if node==dst:
                self.mincost=min(cost,self.mincost)
                return
            if cost>self.mincost or (node in visited) or K>k:
                return
            
            visited.add(node)

            for d,p in airports[node]:
                dfs(d,cost+p,K+1) 

            visited.remove(node)
        dfs(src,0,0)

        return self.mincost