class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, len(s1)
        i = 0

        while r <= len(s2):
            i += 1
            tempLeft, tempRight = l, r
            print("l + r ptrs", l, r)
            print('checking:', s2[l:r])
            temp1 = s1

            while tempLeft < tempRight:
                print('substring', temp1, tempLeft, tempRight)
                
                currIndex = temp1.find(s2[tempLeft])
                isDuplicate = s1.find(s2[tempLeft])
                print(currIndex, isDuplicate)
                if currIndex != -1:
                    if currIndex != len(temp1) - 1:
                        temp1 = temp1[:currIndex] + temp1[currIndex + 1:]
                    else:
                        temp1 = temp1[:currIndex]
                    tempLeft += 1
                elif isDuplicate != -1:
                    l += s2[l:r].find(s2[tempLeft]) + 1
                    r = l + len(s1)
                    print("checking here", l, r, s2[l:r])
                    break
                else:
                    l = tempLeft + 1
                    r = l + len(s1)
                    break
            
            #print('tempLeft', tempLeft, tempRight)
            if tempLeft == tempRight:
                return True
            
            # if i == 15:
            #     break
        
        return False




        