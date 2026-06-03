class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for n in nums:
            res[n] = res.get(n,0) + 1

        sorted_res = dict(sorted(res.items(), key=lambda item:item[1]))

        return list(sorted_res.keys())[-k:]
