class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minheap=[]

        queue=deque()
        queue.append(points[0])
        remain=set([(i,j) for i,j in points])
        #print(remain, queue)
        
        cost=0
        while queue:
            #print(queue)
            x1,y1=queue.pop()
            remain.remove((x1,y1))
            minheap=[]
            for x2,y2 in remain:
                heapq.heappush(minheap,(abs(x2-x1)+abs(y2-y1),x2,y2))
            if not minheap:
                continue
            dist,x2,y2=heapq.heappop(minheap)
            cost+=dist
            queue.append((x2,y2))
            #print(cost, queue[0])
        
        return cost

            


        