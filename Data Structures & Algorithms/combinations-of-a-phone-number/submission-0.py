class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }

        res = [""]

        for num in digits[::-1]:
            temp = []
            for partial in res:
                for ltr in mapping[int(num)]:
                    temp.append(ltr + partial)
            
            res = temp
        
        return res if len(res) != 1 else []
