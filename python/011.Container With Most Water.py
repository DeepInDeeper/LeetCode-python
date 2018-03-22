class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_c = 0
        i = 0
        j = len(height)-1
        while i < j:
            max_c = max(min(height[i],height[j])*(j-i),max_c)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_c
