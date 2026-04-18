class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # map the airports in graphs 
        graph = defaultdict(list)
        for source, dist in tickets:
            # map with heap to make like as sort
            heapq.heappush(graph[source], dist)

        result = []

        def dfs(airport):
            heap = graph[airport]

            while heap:
                # visiting all outgoing edges 
                next_dist = heapq.heappop(heap)
                dfs(next_dist)

            result.append(airport)    

        dfs("JFK")

        return result[::-1]        
        