class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                day = stack.pop()
                result[day[0]] = i - day[0]
            stack.append((i, n))
        return result