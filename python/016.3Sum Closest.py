class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                result = nums[i] + nums[j] + nums[k]
                if abs(result - target) < abs(res - target):
                    res = result
                if result < target:
                    j += 1
                else:
                    k -= 1
        return res

