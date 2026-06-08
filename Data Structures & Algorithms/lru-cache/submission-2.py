class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.tracker = 0
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key][1] = self.tracker
            self.tracker += 1
            return self.cache[key][0]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity and key not in self.cache:
            minUse = [None, float('inf')]
            for k in self.cache:
                if self.cache[k][1] < minUse[1]:
                    minUse = [k, self.cache[k][1]]
            
            self.cache.pop(minUse[0])

        self.cache[key] = [value, self.tracker]
        self.tracker += 1

        
