class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=set(nums1)
        m=set(nums2)
        a=[]
        for i in n:
            if i in m:
                a.append(i)
        return a