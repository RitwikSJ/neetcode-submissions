import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #pilesPerHour = len(piles) // h
        #bananas = sum(piles)

        maxRate = max(piles)
        l, r = 0, maxRate - 1

        while l < r:
            m = l + ((r - l) // 2)

            if not self.validateRate(m + 1, piles, h):
                l = m + 1
            else:
                r = m
        
        return rateChoices[l]
    
    def validateRate(self, rate, piles, h):
        hrsTaken = 0

        for pile in piles:
            print(hrsTaken, math.ceil(pile / rate))
            hrsTaken += math.ceil(pile / rate)
        
        print(rate, hrsTaken, h)
        
        return hrsTaken <= h


        