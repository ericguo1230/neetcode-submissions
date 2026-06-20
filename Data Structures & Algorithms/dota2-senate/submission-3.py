class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        mp = Counter(senate)
        
        idx = 0
        R, D = 0, 0
        while mp['R'] > 0 and mp['D'] > 0:
            if senate[idx] == 'R':
                if R == 0:
                    mp['D'] -= 1
                    D += 1
                else:
                    R -= 1
            else:
                if D == 0:
                    mp['R'] -= 1
                    R += 1
                else:
                    D -= 1
            idx = (idx + 1) % len(senate)
        
        return 'Radiant' if mp['D'] <= 0 else 'Dire'