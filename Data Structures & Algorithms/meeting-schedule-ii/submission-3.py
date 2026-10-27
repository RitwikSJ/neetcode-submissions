"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        events = []

        for i in intervals:
            events.append([i.start, 1])
            events.append([i.end, 0])
        
        events.sort(key=lambda x: (x[0], x[1]))
        # print(events)

        res = 1
        curr = 0

        for i in range(len(events)):
            # print(curr)
            if events[i][1] == 1:
                curr += 1
            else:
                res = max(res, curr)
                curr -= 1
        
        return max(res, curr)
