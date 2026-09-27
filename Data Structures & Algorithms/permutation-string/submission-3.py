class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)

        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1)

        while r <= len(s2):
            window_count = {}
            for c in s2[l:r]:
                window_count[c] = 1 + window_count.get(c, 0)
            if window_count == s1_count:
                return True
            l += 1
            r += 1

        return False


        
        
