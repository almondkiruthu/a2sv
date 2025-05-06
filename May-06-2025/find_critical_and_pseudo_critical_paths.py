class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        # if the node that we are looking at is not a parent of the itself contiue the loop
        while self.par[n] != n:
            # path halving
            self.par[n] = self.par[self.par[n]]
            # move to the grandparent
            n = self.par[n]
        
        return n


    # union function
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
            
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def kruskal(n, edges, skip_idx=None, force_edge=None):
            uf = UnionFind(n)
            cost = 0
            count = 0 # number of edges added

            # force include a specific edge
            if force_edge:
                u, v, w, i = force_edge
                if uf.union(u, v):
                    cost += w
                    count += 1
            
            for u, v, w, i in edges:
                if i == skip_idx:
                    continue
                if uf.union(u, v):
                    cost += w
                    count += 1
                if count == n - 1:
                    break
            
            # if we couldn't connect all nodes return infinity
            if count == n - 1:
                return cost
            else:
                return float("inf")
        
        for i, e in enumerate(edges):
            e.append(i) #[n1, n2, weight, i]
        
        # sort the edges the weight so that we can process the ones that have the minimum cost first
        edges.sort(key=lambda x: x[2])
        
        original_mst_cost = kruskal(n, edges)
        critical = []
        pseudo_critical = []

        for u, v, w, i in edges:
            # check if edge is critical
            cost_without = kruskal(n, edges, skip_idx = i)
            if cost_without > original_mst_cost:
                critical.append(i)
            else:
                # it's non critical-we check if it's pseudo_critical

                cost_with = kruskal(n, edges, force_edge=[u, v, w, i])
                if cost_with == original_mst_cost:
                    pseudo_critical.append(i)

        
        return [critical, pseudo_critical]
