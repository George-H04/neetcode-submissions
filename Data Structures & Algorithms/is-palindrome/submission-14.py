class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed = ""

        for c in s:
            if c.isalnum():
                reversed = c.lower() + reversed

        return reversed == reversed[::-1]