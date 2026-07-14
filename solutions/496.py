class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        ans = {}
        for num in nums2:
            while stack and stack[-1] < num:
                ans[stack[-1]] = num
                stack.pop()
            stack.append(num)
        return [ans.get(num, -1) for num in nums1]
