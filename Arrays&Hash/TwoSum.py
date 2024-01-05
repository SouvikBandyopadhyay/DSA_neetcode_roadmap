class Solution:
    def twoSum(self, nums, target: int):
        h1=dict()
        for index,i in enumerate(nums):
            compi=target-i
            flag=h1.get(compi,"Nil")
            if flag!="Nil":
                return [index,flag]
            else:
                h1[i]=index