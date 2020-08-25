#Find Numbers with Even Number of Digits

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in nums:
            j = str(i)
            l = len(j)
            if l % 2 == 0:
                counter += 1

        return counter