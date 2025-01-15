class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n

        # Construir productos desde la izquierda
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Construir productos desde la derecha y combinar con los de la izquierda
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
