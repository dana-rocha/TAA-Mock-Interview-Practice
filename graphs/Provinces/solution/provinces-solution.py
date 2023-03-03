def num_provinces(is_connected) -> int:
#breadth first search
    # n = len(is_connected)
    # visited = [0] * n
    # ans = 0
    # while not all(visited):
    #     queue = []
    #     for i in range(n):
    #         if not visited[i]:
    #             queue += [i]
    #             break
    #     while queue:
    #         frontier = queue.pop(0)
    #         if not visited[frontier]:
    #             for j in range(n):
    #                 if is_connected[frontier][j]:
    #                     queue += [j]
    #             visited[frontier] = True
    #     ans += 1
    # return ans

            
        def dfs(node):
            for i in range(0,len(is_connected[node])):
                if i != node and is_connected[node][i] == 1 and i not in s:
                    s.add(i)
                    dfs(i)
        
        provinces = 0
        s = set({})
        for i in range(0, len(is_connected)):
            if i not in s:
                s.add(i)
                provinces += 1
                dfs(i)
        return(provinces)
