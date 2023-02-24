def num_provinces(is_connected) -> int:
    def dfs(node, s):
        for i in range(0, len(is_connected[node])):
            if i != node and is_connected[node][i] == 1 and i not in s:
                s.add(i)
                dfs(i, s)
        
    provinces = 0

    s = set({})

    for i in range(0, len(is_connected)):
        if i not in s:
            s.add(i)
            provinces += 1
            dfs(i, s)

    return provinces