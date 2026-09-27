from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.timeMap[key]

        # Binary search find the element
        low = 0
        high = len(timestamps)

        while low != high:
            mid = low + (high - low) // 2

            if timestamps[mid][0] <= timestamp:
                low = mid + 1
            else:
                high = mid

        if low == 0:
            return ""
        else:
            return timestamps[low - 1][1]
