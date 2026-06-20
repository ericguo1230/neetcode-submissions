class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        result = []
        for i in nums:
            mapping[i] += 1
        sorted_mapping = sorted(mapping.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(sorted_mapping[i][0])
        return result