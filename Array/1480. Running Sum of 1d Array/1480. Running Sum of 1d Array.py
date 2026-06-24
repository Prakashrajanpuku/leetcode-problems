class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        c=0
        for i in range (len(nums)):
            c+=nums[i]
            a.append(c)
        return a