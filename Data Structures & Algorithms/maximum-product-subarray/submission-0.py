class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPos = None
        # continuous = True
        tot = None
        currSubBest = -11

        for num in nums:
            if not tot:
                tot = num
            else:
                tot *= num

            if num == 0:
                # if tot is None:
                #     continue
                # elif currSubBest is None:
                #     if maxPos is None:
                #         currSubBest = tot
                #     else:
                #         currSubBest = maxPos
                # else:
                #     if maxPos is None:
                #         currSubBest = max(currSubBest, tot)
                #     else:
                #         currSubBest = max(currSubBest, maxPos)

                choices = []
                if maxPos:
                    choices.append(maxPos)
                choices.append(tot)

                currSubBest = max(currSubBest, max(choices))

                maxPos = None
                # continuous = True
                tot = None

            else:
                if tot > 0:
                    maxPos = tot
                    # continuous = True
                
                elif maxPos and num > maxPos:
                    maxPos = num
                    # continuous = True
            
            print(tot, maxPos)
            
        if maxPos and maxPos > currSubBest:
            return maxPos
        return currSubBest 