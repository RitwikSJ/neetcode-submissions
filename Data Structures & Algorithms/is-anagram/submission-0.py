class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for ltr in s:
            if ltr not in hashS:
                hashS[ltr] = 1
            else:
                hashS[ltr] += 1

        for ltr in t:
            if ltr not in hashT:
                hashT[ltr] = 1
            else:
                hashT[ltr] += 1

        return hashS == hashT