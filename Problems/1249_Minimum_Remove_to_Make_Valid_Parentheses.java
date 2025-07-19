class Solution {
    public String minRemoveToMakeValid(String s) {
        char[] sArray = s.toCharArray();

        int stackLastIndex = -1;
        int[] stack = new int[s.length()];
        
        int resultLastIndex = -1;
        char[] result = new char[s.length()];
        

        for (int i = 0; i < s.length(); i++) {
            char c = sArray[i];
            if (c == '(') {
                result[++resultLastIndex] = c;
                stack[++stackLastIndex] = resultLastIndex;
            } else if (c == ')') {
                if (stackLastIndex >= 0) {
                    stackLastIndex--;
                    result[++resultLastIndex] = c;
                } else {
                    // ignore
                }
            } else {
                result[++resultLastIndex] = c;
            }
            
        }

        if (stackLastIndex >= 0) {
            for (int i = stackLastIndex; i >= 0; i--) {
                int index = stack[i];
                result[index] = '\u0000';
            }
        }

        return new String(result).replace("\u0000", "");
    }
}
