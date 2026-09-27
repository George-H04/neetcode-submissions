class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed = ""
        new_string = [c for c in s if c.isalnum()]

        for c in new_string:
            if not c.isalnum():
                continue
            reversed = c.lower() + reversed

        print(reversed)
        print("".join(new_string))

        return reversed == "".join(new_string).lower()