from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        for i in self.data:
            print(self.data[i])
        closest = []
        if key not in self.data:
            return ""
        
        l, r = 0, len(self.data[key]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if not closest:
                closest = self.data[key][m]
            if self.data[key][m][0] == timestamp:
                # print('hi')
                return self.data[key][m][1]
            elif self.data[key][m][0] < timestamp:
                if min(self.data[key][m][0], closest[0]) == self.data[key][m][0]:
                    closest = self.data[key][m]
                l = m + 1
            else:
                r = m - 1
        # print(closest)
        if closest:
            return closest[1]
        return ""
                    
        
