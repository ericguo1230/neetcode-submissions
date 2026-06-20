class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let result = "";
        for (let word of strs){
            result += word.length + '#' + word;
        }
        return result;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = []
        let i = 0
        while (i < str.length){
            let size = "";
            while (str[i] !== '#'){
                size += str[i];
                i += 1
            }
            size = parseInt(size);
            i = i + 1;
            res.push(str.substring(i, i + size));
            i = i + size;
        }
        return res;
    }
}
