#-*-coding:utf-8-*-
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cleaned_s = "".join(c for c in s if c.isalnum()).lower()

        i = 0
        j = len(cleaned_s) - 1
        while i < j:
            if cleaned_s[i] != cleaned_s[j]:
                return False
            i, j = i + 1, j - 1
        return True
