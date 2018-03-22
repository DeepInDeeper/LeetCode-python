#-*-coding:utf-8-*-
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,len(numbers)-1
        index = [i,j]
        while i < j:
            if numbers[i]+numbers[j] < target:
                i += 1
            elif numbers[i]+numbers[j] > target:
                j -= 1
            else:
                index[0] = i+1
                index[1] = j+1
                return index
