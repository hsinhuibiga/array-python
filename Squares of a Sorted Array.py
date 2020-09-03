#Squares of a Sorted Array

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def f(x):
            return x*x
        return sorted(map(f,A))