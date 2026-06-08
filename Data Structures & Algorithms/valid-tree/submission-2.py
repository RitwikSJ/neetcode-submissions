class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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
        
        path = set()
        visited = set()

        def dfs(node, prev):
            # nonlocal path

            if node in path:
                return False
            
            path.add(node)
            
            if node in adjMap:
                for num in adjMap[node]:
                    if num == prev:
                        continue
                    if dfs(num, node) == False:
                        return False
            
            path.remove(node)
            visited.add(node)
            return True
        
        if dfs(0, None) == False:
            return False
        if len(visited) != n:
            return False
        return True