class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curWindow = maxWindow = 1

        #state (1 is gr and -1 is less than)
        prev_comparison = None
        for idx in range(1, len(arr)):
            curr, prev = arr[idx], arr[idx - 1]
            #We meet a value that is not turbulent
            if prev_comparison is None and curr != prev:
                prev_comparison = False if curr > prev else True
            elif curr == prev:
                curWindow = 1
                prev_comparison = None
                continue
            elif (prev_comparison and curr > prev) or (not prev_comparison and curr < prev):
                curWindow = 1
                prev_comparison = not prev_comparison
            
            curWindow += 1
            prev_comparison = not prev_comparison
            maxWindow = max(maxWindow, curWindow)

        return maxWindow
