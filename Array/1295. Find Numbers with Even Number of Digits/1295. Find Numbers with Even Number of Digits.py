class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=0
        for i in nums:
            c=0
            while i>0:
                i//=10
                c+=1
            if c%2==0:
                r+=1
        return r