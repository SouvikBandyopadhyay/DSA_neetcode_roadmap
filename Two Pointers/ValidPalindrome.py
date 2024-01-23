class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            front = ord(s[i])
            back = ord(s[j])
            if ord(s[i]) > 96 and ord(s[i]) < 123:
                front = ord(s[i])-32
            if ord(s[j]) > 96 and ord(s[j]) < 123:
                back = ord(s[j])-32
            if front > 90 or front < 48 or (front < 65 and front > 57):
                i += 1
                continue
            if back > 90 or back < 48 or (back < 65 and back > 57):
                j -= 1
                continue
            if front != back:
                return False
            i += 1
            j -= 1
        return True
