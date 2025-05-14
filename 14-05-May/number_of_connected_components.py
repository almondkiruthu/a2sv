from collections import defaultdict

class UnionFind:
    def __init__(self, V):
        self.par = {i:i for i in range(V)}
        self.rank = {i:1 for i in range(V)}
        
    def find(self, node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
            
        return node
        
    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return False # alreqdy in the same set or connected component
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1]  = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        return True

class Solution:
    # Function to return connected components of the graph
    def getComponents(self, V, edges):
        # code here
        uf = UnionFind(V)
        for u, v in edges:
            uf.union(u, v)
        
        components = defaultdict(list)  
        #Group nodes by their parent
        for node in range(V):
            parent = uf.find(node)
            components[parent].append(node)
            
        return list(components.values())

if __name__ == "__main__":
    main()

# } Driver Code Ends
