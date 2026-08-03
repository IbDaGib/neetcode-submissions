class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countT = Counter(tasks)
        q = deque()
        heap = []
        for i in countT.values():
            heapq.heappush(heap, -i)

        time = 0
        while heap or q:
            time += 1
            if heap:
                h = 1 + heapq.heappop(heap)
                if h < 0:
                    q.append((h, n + time))
                
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])


        return time