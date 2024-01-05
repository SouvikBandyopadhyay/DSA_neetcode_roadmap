class Solution:
    def productExceptSelf(self, nums):
        mulsum = 1
        zeros = list()
        res = list()
        for index, i in enumerate(nums):
            if i:
                mulsum = mulsum*i
            else:
                zeros.append(index)
        if len(zeros) > 1:
            return [0]*len(nums)
        if len(zeros) > 0:
            res = [0]*len(nums)
            res[zeros[0]] = mulsum
            return res
        else:
            for i in nums:
                res.append(int(mulsum/i))
            return res
