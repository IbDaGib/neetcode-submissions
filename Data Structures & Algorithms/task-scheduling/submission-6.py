class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countT = Counter(tasks)
        q = deque()
        heap = [-i for i in countT.values()]
        heapq.heapify(heap)

        time = 0
        while heap or q:
            time += 1
            if heap:
                h = 1 + heapq.heappop(heap)
                if h < 0:
                    q.append((h, n + time))
            else:
                time = q[0][1]
                
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time