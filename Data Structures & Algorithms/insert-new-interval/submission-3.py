class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart = newInterval[0]
        newEnd = newInterval[1]
        minMerge = None
        maxMerge = None
        placeToInsert = None
        
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            # prevStart, prevEnd = intervals[i - 1][0], intervals[i - 1][1]
            
            print(start, end)
            if start <= newStart and end >= newEnd:
                break
            
            if i >= 1:
                prevEnd = intervals[i - 1][1]
                print('hi', newStart, newEnd, prevEnd, start)
                if newStart > prevEnd and newEnd < start:
                    placeToInsert = i
                    break
            
            if newEnd < start:
                break
            
            if (start >= newStart and end <= newEnd):
                if minMerge is None:
                    minMerge = i
                maxMerge = i
            
            if (start <= newStart and end >= newStart and end <= newEnd):
                if minMerge is None:
                    minMerge = i
                maxMerge = i
                newStart = start
            
            if (start >= newStart and start <= newEnd and end >= newEnd):
                if minMerge is None:
                    minMerge = i
                maxMerge = i
                newEnd = end
        
        print(placeToInsert, maxMerge, minMerge)

        if placeToInsert is not None:
            intervals.insert(placeToInsert, [newStart, newEnd])
        elif minMerge is not None:
            intervals.insert(maxMerge + 1, [newStart, newEnd])
            del intervals[minMerge:maxMerge + 1]
        
        return intervals


            