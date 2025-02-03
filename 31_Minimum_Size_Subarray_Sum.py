class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        total = 0
        min_length = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
            