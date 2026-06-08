class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        res = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            res = max(res, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return res


        