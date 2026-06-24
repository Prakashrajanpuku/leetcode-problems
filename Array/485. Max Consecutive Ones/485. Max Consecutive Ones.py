class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        c1=0
        for i in nums:
            if i==1:
                c+=1
                c1=max(c1,c)
            else:
                c=0
        return c1