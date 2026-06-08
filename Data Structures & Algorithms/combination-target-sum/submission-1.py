class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        path = []

        def dfs(choices, path, summation):
            print(choices, path, summation)
            if summation == target:
                res.append(path)
                return
            if choices == [] or choices[0] > target - summation:
                return
            
            temp = summation
            for i in range(target - temp):
                summation = temp + choices[0] * i
                dfs(choices[1:], path + [choices[0]] * i, summation)
                print(i, summation, summation - choices[0])
                if target - summation - choices[0] < 0:
                    break
        
        dfs(nums, path, 0)
        return res
            



        