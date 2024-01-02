class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(set(nums))!=len(nums)