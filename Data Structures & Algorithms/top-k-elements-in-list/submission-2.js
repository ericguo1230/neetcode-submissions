class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const mp = {}
        const freq = Array.from({length: nums.length + 1}, () => []);
        nums.forEach((number) => {
            mp[number] = (mp[number] || 0) + 1;
        })
        for (const num in mp){
            freq[mp[num]].push(parseInt(num))
        }
        const result = []
        for (let i = freq.length - 1; i > 0; i--){
            for (const n of freq[i]){
                result.push(n);
                if (result.length === k){
                    return result
                }
            }
        }
    }
}
