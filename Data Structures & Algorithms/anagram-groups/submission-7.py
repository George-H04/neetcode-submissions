class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []

        while strs:
            sub = []
            s = strs[0]
            for t in strs[1:]:
                if len(s) != len(t):
                    continue
                hash_s, hash_t = {}, {}
                for c1, c2 in zip(s, t):
                    hash_s[c1] = 1 + hash_s.get(c1, 0)
                    hash_t[c2] = 1 + hash_t.get(c2, 0)
                if hash_s == hash_t:
                    sub.append(t)
                    strs.remove(t)
            sub.append(s)
            strs.remove(s)
            out.append(sub)
        return out
