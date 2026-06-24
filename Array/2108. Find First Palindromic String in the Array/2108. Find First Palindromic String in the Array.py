class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result = ""
        for word in words:
            i = 0
            j = len(word) - 1
            is_pal = True
            while i < j:
                if word[i] != word[j]:
                    is_pal = False
                    break
                i += 1
                j -= 1
            if is_pal:
                result = word
                break
        return result