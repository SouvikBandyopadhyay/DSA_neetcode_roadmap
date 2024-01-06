class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for i in strs:
            temp = str(len(i))+i
            res += temp
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        strs = list()
        pointer = 0
        while (pointer < len(str)):
            try:
                lenofstr = int(str[pointer])
            except:
                lenofstr = 0
            temp = str[pointer+1:pointer+lenofstr+1]
            strs.append(temp)

            pointer = pointer+lenofstr+1
        # write your code here
        return strs
        pass


sn = Solution()
arr = ["ASD5", "aaaaaa", "bbbbbbbbb", "cc", "", "", "", "0", "0", "l;", "\n"]
print(arr)
print(sn.decode(sn.encode(arr)))
