class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        unique = sorted(list(set(hand)))
        freq_counts = dict()

        for i in hand:
            if i not in freq_counts:
                freq_counts[i] = 1
            else:
                freq_counts[i] += 1
        
        while freq_counts:
            curr_min = unique[0]
            print(curr_min, freq_counts)

            for num in range(curr_min, curr_min + groupSize):
                if num not in freq_counts:
                    print(num, "exiting")
                    return False
                
                if freq_counts[num] == 1:
                    freq_counts.pop(num)
                    unique.remove(num)
                else:
                    freq_counts[num] -= 1
        
        return True