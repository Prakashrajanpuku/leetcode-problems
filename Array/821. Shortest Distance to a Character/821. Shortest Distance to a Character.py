class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        positions = []
        for i in range(len(s)):
            if s[i] == c:
                positions.append(i)
        result = [0] * len(s)
        for i in range(len(s)):
            best = abs(i - positions[0])
            for p in positions:
                if abs(i - p) < best:
                    best = abs(i - p)
            result[i] = best
        return result