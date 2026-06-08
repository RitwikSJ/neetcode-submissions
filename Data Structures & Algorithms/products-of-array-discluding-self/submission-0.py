import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        zero_prod = 0
        zero_count = []

        for idx, num in enumerate(nums):
            if num == 0:
                zero_count.append((idx, num))
            if len(zero_count) > 1:
                return [0] * len(nums)
        
        if len(zero_count) == 1:
            nums.pop(zero_count[0][0])
            arr_prod = int(math.prod(nums))
            return [0] * zero_count[0][0] + [arr_prod] + [0] * (len(nums) - zero_count[0][0])

        arr_prod = int(math.prod(nums))
        print(arr_prod, type(arr_prod))
        for i in nums:
            result.append(int(arr_prod / i))
        
        print(result)
        return result

        


        