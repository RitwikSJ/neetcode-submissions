class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()

        for i in range(len(target)):
            res.add(i)

        for trip in triplets:
            if not res:
                break
            
            temp = [a - b for a, b in zip(target, trip)]
            canUse = True

            for num in temp:
                if num < 0:
                    canUse = False
            
            print(res, canUse)
            
            if canUse:
                for i in range(len(temp)):
                    if temp[i] == 0 and i in res:
                        res.remove(i)
                    
        return len(res) == 0