from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mp = defaultdict(int)
        num_swaps_needed = 0
        max_char = ['', 0]
        max_len = 0

        for r in range(len(s)):
            mp[s[r]] += 1

            if mp[s[r]] > max_char[1]:
                max_char[0] = s[r]
                max_char[1] = mp[s[r]]

            num_swaps_needed = (r - l + 1) - max_char[1]
            print(num_swaps_needed, s[l:r + 1])

            if num_swaps_needed > k:
                while l < r and num_swaps_needed > k:
                    mp[s[l]] -= 1
                    if mp[s[l]] != max_char[0]:
                        num_swaps_needed -= 1
                    else:
                        max_char = [max(mp), max(mp.values())]
                        num_swaps_needed = (r - 1 + 1) - max_char[1]
                    l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len

            

            
        