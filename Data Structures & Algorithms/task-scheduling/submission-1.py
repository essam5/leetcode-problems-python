class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1- making a count for getting most freq 
        # 2- we need to use a max heap to get the most freq
        # 3- making a queue that represent pair of 
        # [remaining_count_after_running, idletime]
        # the idletime that represent the index or the time that 
        # we can pop from our queue 
        # so the time will be o(n * m) n represent tasks and q represent the 
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        max_heap = [cnt for cnt in count.values()]
        heapq.heapify_max(max_heap)

        queue = deque() # pair --> [remianing_count, idle_time]
        time = 0 # as a count
        while max_heap or queue:
            time +=1
            if max_heap:
                remaining_count = heapq.heappop_max(max_heap) - 1
                if remaining_count: # if not == 0 because if we found it 0 so we didn't need it
                    queue.append([remaining_count, time + n]) # that the time will use this again

            if queue and queue[0][1] == time:
                # that the time should we pop
                queue_poped = queue.popleft()
                # adding the poped in the heap again with the remaining count
                heapq.heappush_max(max_heap, queue_poped[0])

        return time        



