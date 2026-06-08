class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        canSegment = set()

        for i in range(len(s) - 1, -1, -1):
            for chunk in canSegment:
                if chunk > i and s[i:chunk] in wordDict:
                    canSegment.add(i)
                    break
            
            if i not in canSegment:
                if s[i:] in wordDict:
                    canSegment.add(i)
        
        return 0 in canSegment