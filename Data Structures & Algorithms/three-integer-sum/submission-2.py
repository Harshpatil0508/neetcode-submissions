class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for f in range(len(nums)):
            # skip duplicates for f
            if f > 0 and nums[f] == nums[f - 1]:
                continue

            l = f + 1
            r = len(nums) - 1

            while l < r:
                total = nums[f] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[f], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicates (left)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # skip duplicates (right)
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return res