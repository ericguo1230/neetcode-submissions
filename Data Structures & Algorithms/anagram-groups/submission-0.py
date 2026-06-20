class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for i in strs:
            mapping[tuple(sorted(i))].append(i)
        return list(mapping.values())