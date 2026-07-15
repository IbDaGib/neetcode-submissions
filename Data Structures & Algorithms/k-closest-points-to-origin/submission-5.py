class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for x,y in points:
            d = math.sqrt((x*x) + (y*y))
            heapq.heappush(dist, (-d,[x,y]))
        
        while len(dist) > k:
            heapq.heappop(dist)

        return [coord[1] for coord in dist]