class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countT = Counter(tasks)
        maxheap = [cnt for cnt in countT.values()]
        heapq.heapify_max(maxheap)
        
        res = 0
        q = deque()
        while maxheap or q:
            res += 1
            if maxheap:
                cnt = heapq.heappop_max(maxheap) - 1
                if cnt:
                    q.append([cnt, res + n])
            
            if q and q[0][1] == res:
                heapq.heappush_max(maxheap, q.popleft()[0])
        return res
        

            
        