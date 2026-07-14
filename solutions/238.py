class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        right = 1
        for i in range(n - 1, -1, -1):
            prefix[i] *= right
            right *= nums[i]
        return prefix
