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

                choice = -11
                if maxPos:
                    choice = maxPos
                else:
                    choice = tot

                currSubBest = max(currSubBest, choice)

                maxPos = None
                # continuous = True
                tot = None

            else:
                if tot > 0:
                    maxPos = tot
                    # continuous = True
                
                elif (maxPos and num > maxPos) or (not maxPos and num > 0):
                    maxPos = num
                    # continuous = True
            
            print(tot, maxPos, currSubBest)
        
        choice = -11
        if maxPos is not None:
            choice = maxPos
        elif tot is not None:
            choice = tot

        if currSubBest is not None:
            return max(currSubBest, choice)
        return choice 