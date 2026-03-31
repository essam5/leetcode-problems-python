class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited_map = {i:[] for i in range(n)}

        for n1, n2 in edges:
            visited_map[n1].append(n2)
            visited_map[n2].append(n1)
        
        visited = [False] * n

        def dfs(node):
            for nei in visited_map[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        result = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                result +=1

        return result        

        