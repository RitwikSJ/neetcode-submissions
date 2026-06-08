class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n   # size of each tree

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False  # already connected

        # weighted union (attach smaller tree to larger)
        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA

        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for a, b in edges:
            if uf.find(a - 1) == uf.find(b - 1):
                return [a, b]
            
            uf.union(a - 1, b - 1)        