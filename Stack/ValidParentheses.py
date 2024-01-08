class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"{": "}", "[": "]", "(": ")"}
        seen = list()
        for i in s:
            if i in dic:
                seen.append(dic[i])
            else:
                if len(seen) == 0 or i != seen.pop():
                    return False
        if len(seen) != 0:
            return False
        return True
