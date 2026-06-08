class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = dict()
        res = []

        for i in range(len(s)):
            if s[i] not in pos:
                pos[s[i]] = [i, i]
            else:
                pos[s[i]][1] = i
        
        start, end = pos[s[0]]

        while start <= len(s) - 1:
            for i in range(start + 1, end + 1):
                if pos[s[i]][1] > end:
                    end = pos[s[i]][1]
            res.append(end - start + 1)
            start = end + 1
            if start <= len(s) - 1:
                end = pos[s[start]][1]
        
        return res