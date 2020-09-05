#Check If N and Its Double Exist

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        l = len(arr)
        for i in range(l):
            for j in range(l):
                if (arr[j] == 2*arr[i]) and (i != j):
                    return True
        return False