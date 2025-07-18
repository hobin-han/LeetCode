// https://leetcode.com/problems/longest-common-prefix?envType=problem-list-v2&envId=array

/*
[My Solution] Beats 63.57%
Time Complexity: O(n * m)
Space Complexity: O(m)
*/
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String minStr = strs[0];
        if (minStr == "") return "";

        for (String str: strs) {
            if (str.length() < minStr.length()) {
                minStr = str;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < minStr.length(); i++) {
            for (String str : strs) {
                if (str.charAt(i) != minStr.charAt(i)) return sb.toString();
            }
            sb.append(minStr.charAt(i));
        }
        return sb.toString();
    }
}

/*
[Others' Solution] Beats 100%
Time Complexity: O(n * m)
Space Complexity: O(m)
*/
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        
        String prefix = strs[0];
        for (String s : strs)
            while (s.indexOf(prefix) != 0)
                prefix = prefix.substring(0, prefix.length() - 1);
        return prefix;
    }
}
