#-*-coding:utf-8-*-
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        for i in range(int(len(nums) / 3)):
            if nums[3 * i] != nums[3 * i + 1]:
                return nums[3 * i]
        return nums[-1]


num = [1]
a = Solution()
num_print = a.singleNumber(num)
print(num_print)


