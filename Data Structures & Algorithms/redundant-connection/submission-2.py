class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # visit = [False] * (n + 1)
        cycle = set()
        # cycleStart = -1

        def dfs(node, par):
            # nonlocal cycleStart
            if node in cycle:
                # cycleStart = node
                return True

            # visit[node] = True
            cycle.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            cycle.remove(node)
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []