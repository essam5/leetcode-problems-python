class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency of prerequisites
        # a course has three possible status
        # visited --> a crs has been add to visit
        # visiting -> a crs has added to output and added to cycle
        # unvisited -> a crs not added to output or cycle 
        pre_req = {crs: [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            pre_req[crs].append(pre)

        output, visit, cycle = [], set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)

            for pre in pre_req[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return output                                
                        

