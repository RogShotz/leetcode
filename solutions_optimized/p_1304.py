# Given an integer n, return any array containing n unique integers such that they add up to 0.
#
# Constraints:
#
# 1 <= n <= 1000

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret_arr = []
        for i in range(1, n//2 + 1):
            ret_arr.append(-i)
            ret_arr.append(i)
        if n % 2 == 1:
            ret_arr.append(0)
        
        return ret_arr