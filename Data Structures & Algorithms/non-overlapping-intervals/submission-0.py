class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        #greedily remove the interval with the higher end time
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            if interval[0] < res[-1][1]:
                if interval[1] > res[-1][1]:
                    continue
                res[-1] = interval
            else:
                res.append(interval)
        return len(intervals) - len(res)
