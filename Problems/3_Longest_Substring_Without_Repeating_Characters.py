class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        r = 0
        contained = []

        for c in list(s):
            if c in contained:
                new_r = len(contained)
                if new_r > r:
                    r = new_r
                i = self.findFirstIndex(contained, c)
                contained = contained[i + 1:]
            contained.append(c)

        new_r = len(contained)
        if new_r > r:
            r = new_r
        return r

    def findFirstIndex(self, list, c):
        for i, l in enumerate(list):
            if l == c:
                return i
