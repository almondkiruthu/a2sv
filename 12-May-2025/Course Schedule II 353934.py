# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for crs, preq in prerequisites:
            adj[crs].append(preq)
        
        res = []
        visit = set()
        path = set()

        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            path.add(crs)
            for preq in adj[crs]:
                if not dfs(preq):
                    return False
            path.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res