class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s=set(nums)
        s=list(s)
        s=sorted(s)
        if len(s)<3:
            return max(s)
        else:
            return s[-3]