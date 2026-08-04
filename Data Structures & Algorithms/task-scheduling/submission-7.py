class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        count = Counter(tasks)
        heap = [-i for i in count.values()]
        heapq.heapify(heap)
        time = 0
        while q or heap:
            time += 1
            if not heap:
                time = q[0][1]
            else:
                h = 1 + heapq.heappop(heap)
                if h < 0:
                    q.append((h, n + time))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time