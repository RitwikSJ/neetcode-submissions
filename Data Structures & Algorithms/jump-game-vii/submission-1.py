class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        minClosest = len(s) - 1
        closest = {minClosest}

        for i in range(len(s) - 2, -1, -1):
            # print(closest)
            if s[i] == '1':
                continue

            if i + maxJump < minClosest:
                return False
            
            for j in range(minJump, maxJump + 1):
                if i + j in closest:
                    closest.add(i)
                    minClosest = i
                    break

            if i + maxJump in closest:
                closest.remove(i + maxJump)
                        
        return minClosest == 0
