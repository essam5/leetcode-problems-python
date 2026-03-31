class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited_map = {i:[] for i in range(n)}

        for n1, n2 in edges:
            visited_map[n1].append(n2)
            visited_map[n2].append(n1)
        
        visited_set = set()

        def dfs(node, prev):
            if node in visited_set:
                return False

            visited_set.add(node)

            for nei in visited_map[node]:
                if nei == prev:
                    continue

                if not dfs(nei, node):
                    return False
            return True                

        return dfs(0, -1) and len(visited_set) == n   
            
























        visited_map = {i: [] for i in range(n)}
        for n1, n2 in edges:
            visited_map[n1].append(n2)
            visited_map[n2].append(n1)
        visited_set = set()

        def dfs(n, prev):
            if n in visited_set:
                return False
            visited_set.add(n)
            for i in visited_map[n]:
                if i == prev:
                    continue
                if not dfs(i, n):
                    return False
            return True                

        return dfs(0, -1) and len(visited_set) == n    
        