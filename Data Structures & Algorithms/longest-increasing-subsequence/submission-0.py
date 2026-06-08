class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        candidates = []
        maxElement = -1001
        seen = set()
        s = 0

        for i in range(len(nums) - 1, -1, -1):
            s += 1
            if s < 15:
                print(candidates)
            else:
                break
            if nums[i] > maxElement:
                maxElement = nums[i]
                candidates.append([nums[i]])
                continue
            if nums[i] in seen:
                continue
            
            for c in range(len(candidates)):
                if nums[i] < candidates[c][0]:
                    if nums[i] < candidates[c][-1]:
                        candidates[c].append(nums[i])
                    else:
                        temp = []
                        print('erer')
                        for num in candidates[c]:
                            if num > nums[i]:
                                temp.append(num)
                            else:
                                break
                        temp.append(nums[i])
                        candidates.append(temp)
            
            seen.add(nums[i])
        
        res = 0

        for cand in candidates:
            res = max(res, len(cand))
        
        return res