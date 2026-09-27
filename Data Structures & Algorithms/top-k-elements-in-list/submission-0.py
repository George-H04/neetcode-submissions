class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1

        sorted_frequency = [key for key, val in sorted(hash.items(), reverse=True, key=lambda item: item[1])]

        return sorted_frequency[:k]
        