class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(path, choices):
            if choices == []:
                res.append(path[:])
                return
            
            for i in range(len(choices)):
                path.append(choices[i])
                print(path, choices)
                if i != len(choices) - 1:
                    dfs(path, choices[:i] + choices[i + 1:])
                else:
                    dfs(path, choices[:i])
                path.pop()
        
        dfs(path, nums)

        return res