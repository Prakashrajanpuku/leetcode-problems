class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = [0] * 26
        
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        for ch in t:
            count[ord(ch) - ord('a')] -= 1
        
        for i in range(26):
            if count[i] != 0:
                return chr(i + ord('a'))