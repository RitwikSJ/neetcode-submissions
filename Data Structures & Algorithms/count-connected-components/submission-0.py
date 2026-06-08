class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        adjMap = dict()

        for a, b in edges:
            if a not in adjMap:
                adjMap[a] = {b}
            else:
                adjMap[a].add(b)
            
            if b not in adjMap:
                adjMap[b] = {a}
            else:
                adjMap[b].add(a)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)

            if node in adjMap:
                for nei in adjMap[node]:
                    if nei != prev:
                        dfs(nei, node)
        
        for i in range(n):
            if i not in visited:
                dfs(i, None)
                components += 1
        
        return components
        