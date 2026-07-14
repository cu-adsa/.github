class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = set()
        for i, num in enumerate(nums):
            if i > k:
                seen.remove(nums[i - k - 1])
            if num in seen:
                return True
            seen.add(num)
        return False
