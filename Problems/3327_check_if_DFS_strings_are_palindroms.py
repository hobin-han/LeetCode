class Node:
    def __init__(self):
        self.start = None
        self.end = None

    def set_start(self, s):
        if self.start is None:
            self.start = s

    def set_end(self, e):
        if self.end is None:
            self.end = e

    def is_palindrome(self, string, start, end):
        if start is None:
            return True

        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True


class Solution(object):

    def findAnswer(self, parent, s):
        nodes = []
        new_parent = {}
        for i, p in enumerate(reversed(parent)):
            # nodes
            nodes.append(Node())
            # new_parent
            new_i = len(parent) - 1 - i
            if not p in new_parent:
                new_parent[p] = []
            new_parent[p].append(new_i)
        
        stack = []
        string = []
        current = -1
        while len(string) < len(s):
            if current not in new_parent or len(new_parent[current]) == 0:
                # None
                index = len(string)
                for i in stack:
                    if i >= 0:
                        nodes[i].set_start(index)
                nodes[current].set_end(index)
                string.append(s[current])
                current = stack.pop()
                continue
            
            # not None
            current_i = new_parent[current].pop()
            # stack
            stack.append(current)
            
            current = current_i

        return [n.is_palindrome(string, n.start, n.end) for i, n in enumerate(nodes)]

'''
current = parent[current_i]
parent_new[current].pop() = current_i

last of current_i = current_i
first = current
---------------------------------------------------------------
-1  = parent[0]                                 #
0   = parent[1], stack: [0]                     #
1   = parent[3], stack: [0, 1]                  #
3   = None, dfsStr = [3]                        # 3 = first(0, 1), 3 = last(3)
1   = parent[4], stack: [0, 1]                  # 
4   = None, dfsStr = [3, 4]                     # 4 = last(4)
1   = None, dfsStr = [3, 4, 1]                  # 1 = last(1)
0   = parent[2], stack: [0]                     # 
2   = parent[5], stack: [0, 2]                  # 
5   = None, dfsStr = [3, 4, 1, 5]               # 5 = first(2), 5 = last(5)
2   = None, dfsStr = [3, 4, 1, 5, 2]            # 2 = last(2)
0   = None, dfsStr = [3, 4, 1, 5, 2, 0]         # 0 = last(0)
'''

parent = [-1,0,0,1,1,2]
s = "aababa"
print(Solution().findAnswer(parent, s))
