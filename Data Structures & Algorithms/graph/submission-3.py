class Graph:
    
    def __init__(self):
        self.adjList = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList:
            return False
        self.adjList[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)

    def dfs(self, src, dst, visited) -> bool:
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adjList.get(src, []):
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited):
                    return True
        return False

    def bfs(self, src, dst) -> bool:
        visited = set()
        q = deque([src])
        while q:
            cur = q.popleft()
            if cur == dst:
                return True
            visited.add(cur)
            for neighbore in self.adjList.get(cur, []):
                if neighbore not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return False

