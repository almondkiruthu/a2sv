# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, n):
        self.par = {i:i for i in range(1, n + 1)}
        self.rank = {i:0 for i in range(1, n + 1)}

    def find(self, node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]

        return node

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        uf = UnionFind(n)
        res = []

        for a, b in edges:
            if not uf.union(a,b):
                res.append((a, b))

        if len(res) > 1:
            return res[-1]
        else:
            return res.pop()


        