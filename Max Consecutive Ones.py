#Max Consecutive Ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = -1
        N = len(nums)
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                index = i
            else:
                res = max(res, i - index)
        return res