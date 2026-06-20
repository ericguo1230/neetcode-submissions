class TimeMap:

    def __init__(self):
        self.timestamp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp[key].append((value, timestamp))
        return None

    def get(self, key: str, timestamp: int) -> str:
        val, time = 0, 1
        if not self.timestamp[key]:
            return ""
        if timestamp >= self.timestamp[key][-1][time]:
            return self.timestamp[key][-1][val]

        left, right = 0, len(self.timestamp[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.timestamp[key][mid][time] <= timestamp and self.timestamp[key][mid + 1][time] > timestamp:
                return self.timestamp[key][mid][val]
            elif self.timestamp[key][mid][time] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return ""