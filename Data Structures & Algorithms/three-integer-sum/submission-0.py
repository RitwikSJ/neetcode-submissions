class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        nums.sort()

        for i in range(len(nums)):
            target = 0 - nums[i]

            left = 0
            right = len(nums) - 1

            while left < right:
                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue

                if nums[left] + nums[right] == target:
                    print((nums[i], nums[left], nums[right]))
                    if i < left:
                        result.add((nums[i], nums[left], nums[right]))
                    elif i > right:
                        result.add((nums[left], nums[right], nums[i]))
                    else:
                        result.add((nums[left], nums[i], nums[right]))
                    break
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        
        return list(result)

        