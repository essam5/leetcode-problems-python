class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_map = defaultdict(list)
        for u, v, t in times: #O(time) I mean egdes so O(E)
            time_map[u].append((v, t)) # pair of node target, time

        time = 0
        min_heap = [(0, k)] # pair of time, start node
        visited = set()  

        while min_heap: # O(E) * O(log n) not O(n) * o(log n) because node 
        # node could push multiple time
            time_1, node_1 = heapq.heappop(min_heap)

            if node_1 in visited:
                continue
            visited.add(node_1)
            time = time_1 # recent time

            for node_2, time_2 in time_map[node_1]:
                if node_2 not in visited:
                    heapq.heappush(min_heap, (time_2 + time_1, node_2))

        return time if len(visited) == n else -1            




        