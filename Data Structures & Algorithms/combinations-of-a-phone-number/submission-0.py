class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
            2: ['a','b','c'],
            3: ["d", 'e', 'f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }
        result = []

        def backtrack(i, res):
            if len(res) >= len(digits):
                result.append(res)
                return
            for c in mp[int(digits[i])]:
                backtrack(i + 1, res + c)

        if digits:     
            backtrack(0, "")
        return result