class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges=defaultdict(list)
        for i in times:
            edges[i[0]].append([i[1],i[2]])

        res=0
        minheap=[]
        minheap.append((k,0))
        visited=set()

        while minheap:
            node,time=heapq.heappop(minheap)

            if node in visited:
                continue
            visited.add(node)
    
            res=max(res,time)
            for i,j in edges[node]:
                heapq.heappush(minheap,(i,j+time))
        
        if len(visited)<n:
            return-1
        
        return res
        