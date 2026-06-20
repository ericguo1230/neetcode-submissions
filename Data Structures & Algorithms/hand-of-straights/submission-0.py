class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True

        mp = defaultdict(int)
        
        for card in hand:
            mp[card] += 1
        
        tot = 1
        handSize = 1
        curMin = min(hand)
        mp[curMin] -= 1

        while tot < len(hand):
            print(curMin, handSize, tot)
            print(mp)
            if handSize == groupSize:
                curMin = min(mp)
                while mp[curMin] == 0:
                    mp.pop(curMin)
                    curMin = min(mp)
                mp[curMin] -= 1
                handSize = 1
                tot += 1
            else:
                if curMin + 1 in mp and mp[curMin + 1] > 0:
                    mp[curMin + 1] -= 1
                    tot += 1
                    handSize += 1
                    curMin = curMin + 1
                else:
                    return False
        return handSize == groupSize
                