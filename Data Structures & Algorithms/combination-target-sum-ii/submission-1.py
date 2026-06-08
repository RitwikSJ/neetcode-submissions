class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = set()
        path = []

        def dfs(path, summation, i):
            if summation == target:
                res.add(tuple(path[:]))
                return
            if i == len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j == 4:
                    print('5 in contention', path)
                if path == [] and j != 0 and candidates[j] == candidates[j - 1]:
                    continue
                
                if summation + candidates[j] > target:
                    print('breaking', path, candidates[i])
                    break
                path.append(candidates[j])
                dfs(path, summation + candidates[j], j + 1)
                path.pop()
                #print(i, j)
        
        dfs(path, 0, 0)
        
        res = list(res)
        for i in range(len(res)):
            print(list(res[i]), res[i])
            res[i] = list(res[i])
        print(res)
        return res
        