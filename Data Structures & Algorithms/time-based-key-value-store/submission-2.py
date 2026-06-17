class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list) # key: (timestamp, value)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.timestamps[key])-1
        # timestamp is basically target
        res = ""
        while l <= r:
            m = (l+r) // 2
            if self.timestamps[key][m][0] <= timestamp:
                res = self.timestamps[key][m][1]
                l = m + 1
            else:
                r = m - 1

        return res



        
