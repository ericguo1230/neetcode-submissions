class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = {}
        for i in range(len(position)):
            mp[position[i]] = speed[i]
        position.sort()
        stack = []
        for i in range(len(position) - 1, -1, -1):
            time = (target - position[i]) / mp[position[i]]
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        return len(stack)