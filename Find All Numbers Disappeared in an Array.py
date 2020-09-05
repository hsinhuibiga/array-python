#Find All Numbers Disappeared in an Array

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        numset = set(nums)
        N = len(nums)
        for num in range(1, N + 1):
            if num not in numset:
                res.append(num)
        return res