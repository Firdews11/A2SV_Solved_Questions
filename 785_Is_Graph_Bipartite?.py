class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1 for _ in range(len(graph))]
        res = True
        def dfs(parent):
            temp = True
            for nei in graph[parent]:
                if colors[nei] == -1:
                    colors[nei] = 1 - colors[parent]
                    temp = temp and dfs(nei)
                elif colors[nei] == colors[parent]:
                    return False
            return temp
                

        for i, color in enumerate(colors):
            if color == - 1:
                colors[i] = 0
                res = res and dfs(i)
                
        return res
