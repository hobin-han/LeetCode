class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = []
        for p in path.split('/'):
            if p == "" or p == ".":
                continue

            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
                    
        result = '/'.join(stack)
        result = "/" + result
        return result