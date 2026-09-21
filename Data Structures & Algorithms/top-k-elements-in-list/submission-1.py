from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sortedFreq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        res = []
        for i in sortedFreq:
            if len(res)<k:
                res.append(i)
        return res