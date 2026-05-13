class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for c in nums:
            res[c] = res.get(c,0)+1
        
        sorted_res = dict(sorted(res.items(),key=lambda item:item[1]))

        return list(sorted_res.keys())[-k:]