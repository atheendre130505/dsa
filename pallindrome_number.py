class Solution(object):
    def isPalindrome(self, x):
        x=[i for i in str(x)]
        length=len(x)
        is_palindrome=True

        for i in range(length//2):
            if x[i] != x[length-1-i]:
                is_palindrome=False
                break
        return is_palindrome

        """
        :type x: int
        :rtype: bool
        """
        