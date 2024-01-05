class Solution:
    def topKFrequent(self, nums, k: int):
        dic = dict()
        for i in nums:
            dic[i] = dic.get(i, 0)+1
        res = [i[0]
               for i in sorted(dic.items(), key=lambda x: x[1], reverse=True)]
        return res[:k]
