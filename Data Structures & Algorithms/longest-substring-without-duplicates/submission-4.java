class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int result = 0;
        for (int right = 0; right < s.length(); right ++){
            String substring = s.substring(left, right);
            while (substring.indexOf(s.charAt(right)) != -1){
                left += 1;
                substring = s.substring(left, right);
            }
            if (substring.length() + 1 > result){
                result = substring.length() + 1;
            }
        }
        return result;
    }
}
