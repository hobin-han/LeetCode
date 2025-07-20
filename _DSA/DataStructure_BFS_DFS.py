'''
DFS - Depth First Search, Use Stack         (ex) binary tree traversal - inorder, preorder, postorder
BFS - Breadth First Search, Use Queue
'''

graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1],
    3: [0, 4, 5],
    4: [3],
    5: [3]
}
   
def bfs(graph):
    if len(graph) == 0:
        return
    
    q_index = 0
    queue = [0]
    
    while q_index < len(queue):
        c_num = queue[q_index]
        print(c_num)

        for n_num in graph[c_num]:
            if not n_num in queue:
                queue.append(n_num)

        q_index += 1

print("-> breadth first search")
bfs(graph)

def dfs(graph):
    if len(graph) == 0:
        return
    
    used = set([])
    stack = []
    c_num = 0
    while True:
        if not c_num in used:
            print(c_num)
            used.add(c_num)

        is_c_num_updated = False
        for n_num in graph[c_num]:
            if n_num not in used:
                stack.append(c_num)
                c_num = n_num
                is_c_num_updated = True
                break
        
        if len(stack) == 0:
            return
        elif not is_c_num_updated:
            c_num = stack.pop()

print("-> depth first search")
dfs(graph)

print("------------------------")
# ------ Tips

# reverse String
print("(revers string)", ''.join(reversed("abcd")))


# set
set_num = set([1, 3, 4, 1, 2])
print("(set num)", set_num)

# not in
print("(not in 1)", 1 not in [1, 2, 3])
print("(not in 2)", not 2 in [1, 2, 3])