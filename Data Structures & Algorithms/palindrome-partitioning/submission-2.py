class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(start, end, path):
            print(start, end, path)
            if end >= len(s):
                path.append(s[start:end])
                if start != 0:
                    if s[start:end] == s[end - 1:start - 1:-1]:
                        res.append(path[:])
                else:
                    if s[start:end] == s[end - 1::-1]:
                        res.append(path[:])
                path.pop()
                return

            if start != 0:
                # print(s[start:end], s[end:start - 1:-1])
                if s[start:end] == s[end - 1:start - 1:-1]:
                    path.append(s[start:end])
                    print('found palin1')
                    dfs(end, end + 1, path)
                    path.pop()
            else:
                # print(s[start:end], s[end - 1::-1])
                if s[start:end] == s[end - 1::-1]:
                    path.append(s[start:end])
                    print('found palin2')
                    dfs(end, end + 1, path)
                    path.pop()

            print('extend')
            dfs(start, end + 1, path)
        
        dfs(0, 1, path)

        return res

