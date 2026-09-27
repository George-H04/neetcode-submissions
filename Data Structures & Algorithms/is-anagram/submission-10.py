class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}
        
        for c1, c2 in zip(s, t):
            hash_s[c1] = hash_s.get(c1, 0) + 1
            hash_t[c2] = hash_t.get(c2, 0) + 1
        
        return hash_s == hash_t


