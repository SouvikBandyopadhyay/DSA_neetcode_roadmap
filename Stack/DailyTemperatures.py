class Solution:
    def dailyTemperatures(self, temperatures):
        stack = list()
        dic = dict()
        for index, i in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(index)
            else:
                while len(stack):
                    if temperatures[stack[-1]] < i:
                        pos = stack.pop()
                        dic[pos] = index
                    else:
                        break
                stack.append(index)
        res = list()
        for i in range(len(temperatures)):
            res.append(dic.get(i, i)-i)
        return res
