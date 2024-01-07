class Solution:
    def longestConsecutive(self, nums) -> int:
        nums=sorted(set(nums))
        lis=list()
        temp=0
        for index,i in enumerate(nums):
            if index==0:
                temp=1
            if index>0:
                if i==nums[index-1]+1:
                    temp=temp+1
                else:
                    lis.append(temp)
                    temp=1
        lis.append(temp)
        return max(lis)
