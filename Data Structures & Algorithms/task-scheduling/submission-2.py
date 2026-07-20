class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = list(Counter(tasks).values())
        heapq.heapify_max(heap)
        
        time = 0
        q = deque()
        while heap or q:
            time += 1
            if heap:
                cnt = heapq.heappop_max(heap) - 1
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(heap, q.popleft()[0])
        return time
        

            
        