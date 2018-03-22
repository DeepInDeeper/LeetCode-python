#-*-coding:utf-8-*-
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if val not in nums:
            return len(nums)
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
