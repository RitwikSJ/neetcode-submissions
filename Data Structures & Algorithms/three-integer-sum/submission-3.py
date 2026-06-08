class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = {}
        unique_nums = set()
        final = set()

        nums.sort()

        for num in nums:
            unique_nums.add(num)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i], nums[j]) not in result:
                    result[(nums[i], nums[j])] = [(i, j)]
                else:
                    result[(nums[i], nums[j])].append((i, j))
        
        for key, val in result.items():
            for i in range(len(nums)):
                if nums[i] + key[0] + key[1] == 0:
                    temp = [nums[i], key[0], key[1]]
                    temp.sort()

                    if tuple(temp) in final:
                        continue
                    for idxs in val:
                        if i not in idxs:
                            print(temp, i, idxs)
                            final.add(tuple(temp))
        
        return list(final)


        #     target = 0 - nums[i]

        #     left = 0
        #     right = len(nums) - 1

        #     while left < right:
        #         if left == i:
        #             left += 1
        #             continue
        #         elif right == i:
        #             right -= 1
        #             continue

        #         #print((nums[i], nums[left], nums[right]), i, left, right)
        #         if nums[left] + nums[right] == target:
        #             if i < left:
        #                 result.add((nums[i], nums[left], nums[right]))
        #             elif i > right:
        #                 result.add((nums[left], nums[right], nums[i]))
        #             else:
        #                 result.add((nums[left], nums[i], nums[right]))
        #         elif nums[left] + nums[right] <= target:
        #             left += 1
        #         else:
        #             right -= 1
        
        # return list(result)

        