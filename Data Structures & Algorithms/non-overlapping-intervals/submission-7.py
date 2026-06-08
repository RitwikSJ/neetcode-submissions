class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        new = []
        bestCandidate = None
        res = 0

        for i in range(len(intervals)):
            if bestCandidate is None:
                bestCandidate = intervals[i]
                continue
            
            if intervals[i][0] == bestCandidate[0]:
                if bestCandidate[1] > intervals[i][1]:
                    bestCandidate = intervals[i]
                res += 1
            else:
                new.append(bestCandidate)
                bestCandidate = intervals[i]
        
        if bestCandidate:
            new.append(bestCandidate)
        print(new, res)
        new.sort(key=lambda x: x[1])
        secondNew = []
        bestCandidate = None

        for i in range(len(new)):
            if bestCandidate is None:
                bestCandidate = new[i]
                continue
            
            if new[i][1] == bestCandidate[1]:
                if bestCandidate[1] - bestCandidate[0] > new[i][1] - new[i][0]:
                    bestCandidate = new[i]
                # print(new[i], bestCandidate, i)
                res += 1
            else:
                secondNew.append(bestCandidate)
                bestCandidate = new[i]
        
        if bestCandidate:
            secondNew.append(bestCandidate)
        print(secondNew, res)
        thirdNew = []
        secondNew.sort(key=lambda x: x[0])
        bestCandidate = None
        
        for i in range(len(secondNew)):
            if bestCandidate is None:
                bestCandidate = secondNew[i]
                continue
            
            if secondNew[i][0] < bestCandidate[1]:
                if bestCandidate[1] -bestCandidate[0] > secondNew[i][1] - secondNew[i][0]:
                    bestCandidate = secondNew[i]
                # print(secondNew[i], bestCandidate, i)
                res += 1
            else:
                thirdNew.append(bestCandidate)
                bestCandidate = secondNew[i]
        
        if bestCandidate:
            thirdNew.append(bestCandidate)
        print(thirdNew, res, len(intervals) - len(thirdNew))
        
        return res
