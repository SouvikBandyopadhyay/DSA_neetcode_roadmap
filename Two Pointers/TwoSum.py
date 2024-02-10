class Solution:
    def twoSum(self, numbers, target: int):
        dic=dict()
        for index,i in enumerate(numbers):
            h=dic.get(i,-1)
            if h>=0:
                return [h,index+1]
            dic[target-i]=index+1
