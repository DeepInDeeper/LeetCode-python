#-*-coding:utf-8-*-
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        for i in range(int(len(nums)/2)):
            if nums[2*i] != nums[2*i+1]:
                return nums[2*i]
        return nums[-1]

# of course,simple solution is to use XOR
