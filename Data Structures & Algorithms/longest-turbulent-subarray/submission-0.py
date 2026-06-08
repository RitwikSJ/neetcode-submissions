class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curr = 0
        biggerMid = None
        i = 1
        largest = 2

        if len(arr) <= 2:
            return len(arr)

        while i <= len(arr) - 1:
            print(curr, i, biggerMid)
            if biggerMid is None:
                if arr[i] < arr[i - 1] and (i + 1 == len(arr) or arr[i] < arr[i + 1]):
                    # if curr == 0:
                    #     curr = 3
                    # else:
                    #     curr += 2
                    curr += 3
                    biggerMid = False
                    i += 2
                elif arr[i] > arr[i - 1] and (i + 1 == len(arr) or arr[i] > arr[i + 1]):
                    curr += 3
                    biggerMid = True
                    i += 2
                else:
                    i += 1
            elif biggerMid == True:
                if arr[i] > arr[i - 1] and (i + 1 == len(arr) or arr[i] > arr[i + 1]):
                    curr += 2
                    i += 2

                    if (i - 1 == len(arr)):
                        curr -= 1
                        largest = max(curr, largest)
                else:
                    biggerMid = None
                    i += 1
                    largest = max(curr, largest)
                    curr = 0
            else:
                if arr[i] < arr[i - 1] and (i + 1 == len(arr) or arr[i] < arr[i + 1]):
                    curr += 2
                    i += 2

                    if (i - 1 == len(arr)):
                        curr -= 1
                        largest = max(curr, largest)
                else:
                    biggerMid = None
                    i += 1
                    largest = max(curr, largest)
                    curr = 0
        return largest

