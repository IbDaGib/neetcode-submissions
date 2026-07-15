class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for x,y in points:
            d = math.sqrt((x*x) + (y*y))
            heapq.heappush_max(dist, (d,[x,y]))
        
        while len(dist) > k:
            heapq.heappop_max(dist)

        
        # print(dist[0][:2])

        return [point for d, point in dist]