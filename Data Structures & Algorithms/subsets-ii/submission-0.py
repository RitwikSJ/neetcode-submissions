class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        path = []
        
        def dfs(choices, path):
            if choices == []:
                res.add(tuple(path[:]))
                return
            
            print('before', path, choices)
            dfs(choices[1:], path[:])
            path.append(choices[0])
            print('after', path, choices)
            dfs(choices[1:], path[:])
            path.pop()

        dfs(nums, path)
        print(res)
        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res      
            
