class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        c_list = list(s)
        s_i = 0
        e_i = len(c_list) - 1

        while s_i < e_i:
            s = c_list[s_i].upper()
            e = c_list[e_i].upper()

            if not self.checkIsAlphanumeric(s):
                s_i += 1
            elif not self.checkIsAlphanumeric(e):
                e_i -= 1
            else:
                if s != e: 
                    return False

                s_i += 1
                e_i -= 1

        return True

    def checkIsAlphanumeric(self, char):
        return ord('A') <= ord(char) <= ord('Z') or ord('0') <= ord(char) <= ord('9')