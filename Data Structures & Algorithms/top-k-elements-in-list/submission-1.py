class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        for i in nums:
            mapping[i] += 1
        mapping_list = [0] * (len(nums) + 1)
        result = []
        for i in mapping:
            if mapping_list[mapping[i]] == 0:
                mapping_list[mapping[i]] = [i]
            else:
                mapping_list[mapping[i]].append(i)
        for i in range(len(mapping_list) - 1, -1, -1):
            if mapping_list[i] != 0:
                if len(result) == k:
                    break
                result.extend(mapping_list[i])
        return result