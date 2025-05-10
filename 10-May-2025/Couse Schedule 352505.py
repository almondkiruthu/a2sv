# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        # build the adj list
        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            visit.add(crs)

            for preq in preMap[crs]:
                if not dfs(preq):
                    return False
            # if the path is compeltable remove it from visited so that it can be explored.
            visit.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True