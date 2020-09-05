#Replace Elements with Greatest Element on Right Side

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = [-1]
        max_val = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            res.insert(0,max_val)
            max_val = max(arr[i], max_val)
        return res