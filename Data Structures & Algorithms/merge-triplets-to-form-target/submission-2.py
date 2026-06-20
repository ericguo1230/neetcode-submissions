class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True

        counter = 0
        mp1, mp2, mp3 = defaultdict(list), defaultdict(list), defaultdict(list)
        ref = [mp1, mp2, mp3]
        for a, b, c in triplets:
            mp1[a].append([(b, 1), (c, 2)])
            mp2[b].append([(a, 0), (c, 2)])
            mp3[c].append([(a, 0), (b, 1)])
        
        for i in range(3):
            if target[i] in ref[i]:
                found = False
                for a, b in ref[i][target[i]]:
                    if target[a[1]] >= a[0] and target[b[1]] >= b[0]:
                        found = True
                if not found:
                    return False
            else:
                return False
        return True

