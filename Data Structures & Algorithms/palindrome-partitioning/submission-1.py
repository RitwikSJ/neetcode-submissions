class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        palindromes = []
        path = []

        for i in range(len(s)):
            for j in range(len(s), i + 1, -1):
                if i == 0:
                    print(s[i:j], s[j - 1::-1])
                    if s[i:j] == s[j - 1::-1]:
                        palindromes.append((s[i:j], i))
                else:
                    print(s[i:j], s[j - 1:i - 1:-1])
                    if s[i:j] == s[j - 1:i - 1:-1]:
                        palindromes.append((s[i:j], i))
        
        print(palindromes)

        def dfs(i, path):
            print(i, path)
            if i == len(s):
                res.append(path[:])
                print(path, 'appeneded')
                return
            
            for substr, start in palindromes:
                if start == i:
                    path.append(substr)
                    dfs(i + len(substr), path)
                    path.pop()
                    print(i, path, 'popped loop')

            print(i, path, 'new')
            path.append(s[i])
            dfs(i + 1, path)
            path.pop()
            print(i, path, 'popped')
        
        dfs(0, path)

        return res

        